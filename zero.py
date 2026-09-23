#!/usr/bin/env python3
"""ZERO v0.2 — stateful adversarial explorer for agent tool workflows."""
from __future__ import annotations
import argparse, json
from dataclasses import dataclass, field
from pathlib import Path

@dataclass(frozen=True)
class Action:
    name: str
    spend: int = 0
    reads_private: bool = False
    sends_external: bool = False

@dataclass
class State:
    spend: int = 0
    has_private: bool = False
    trace: list[str] = field(default_factory=list)

def load(path: str):
    raw=json.loads(Path(path).read_text())
    actions=[Action(**x) for x in raw["actions"]]
    return raw, actions

def step(state: State, action: Action):
    return State(state.spend+action.spend,
                 state.has_private or action.reads_private,
                 state.trace+[action.name])

def violations(state: State, rules: dict):
    out=[]
    if state.spend > rules.get("max_total_spend", 10**18):
        out.append({"type":"cumulative_spend","actual":state.spend,
                    "limit":rules["max_total_spend"]})
    if rules.get("forbid_private_external") and state.has_private and state.trace:
        # Violation only when the latest action actually sends externally.
        pass
    return out

def explore(cfg, actions, depth):
    rules=cfg["rules"]; found=[]; frontier=[State()]
    for _ in range(depth):
        nxt=[]
        for s in frontier:
            for a in actions:
                ns=step(s,a); vs=violations(ns,rules)
                if rules.get("forbid_private_external") and s.has_private and a.sends_external:
                    vs.append({"type":"private_data_exfiltration"})
                if vs:
                    found.append({"trace":ns.trace,"violations":vs})
                nxt.append(ns)
        frontier=nxt
    # dedupe by violation class + trace
    seen=set(); unique=[]
    for f in found:
        key=(tuple(f["trace"]),tuple(v["type"] for v in f["violations"]))
        if key not in seen: seen.add(key); unique.append(f)
    return unique

def main():
    p=argparse.ArgumentParser(description="Break your AI agent before production.")
    p.add_argument("scenario"); p.add_argument("--depth",type=int,default=3)
    p.add_argument("--json",action="store_true"); args=p.parse_args()
    cfg,actions=load(args.scenario); findings=explore(cfg,actions,args.depth)
    if args.json: print(json.dumps(findings,indent=2)); return
    print(f"ZERO explored depth={args.depth}; findings={len(findings)}")
    for i,f in enumerate(findings[:20],1):
        print(f"\n[{i}] {' -> '.join(f['trace'])}")
        for v in f["violations"]: print("   VIOLATION:",v["type"],v)
if __name__=="__main__": main()
