#!/usr/bin/env python3
"""Compile a standalone algorithm2e LaTeX file to PDF."""

import subprocess
import sys
from pathlib import Path


def compile_tex(tex_path: str, engine: str = "xelatex") -> dict:
    tex = Path(tex_path).resolve()
    if not tex.exists():
        return {"success": False, "error": f"File not found: {tex}"}

    workdir = tex.parent
    stem = tex.stem
    pdf_path = workdir / f"{stem}.pdf"

    engines = [engine]
    if engine != "pdflatex":
        engines.append("pdflatex")

    for eng in engines:
        cmd = [
            eng,
            "-interaction=nonstopmode",
            "-halt-on-error",
            f"-output-directory={workdir}",
            str(tex),
        ]
        try:
            result = subprocess.run(
                cmd, capture_output=True, text=True, timeout=60, cwd=workdir
            )
            if result.returncode == 0 and pdf_path.exists():
                return {
                    "success": True,
                    "engine": eng,
                    "pdf_path": str(pdf_path),
                    "log": result.stdout[-500:] if len(result.stdout) > 500 else result.stdout,
                }
        except FileNotFoundError:
            continue
        except subprocess.TimeoutExpired:
            continue

    return {
        "success": False,
        "engine": engines[0],
        "error": f"Compilation failed. Tried: {', '.join(engines)}",
        "pdf_path": str(pdf_path) if pdf_path.exists() else None,
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: compile_algo.py <file.tex> [xelatex|pdflatex|latexmk]")
        sys.exit(1)

    tex_path = sys.argv[1]
    engine = sys.argv[2] if len(sys.argv) > 2 else "xelatex"

    result = compile_tex(tex_path, engine)

    if result["success"]:
        print(f"[OK] Compiled with {result['engine']}")
        print(f"     PDF: {result['pdf_path']}")
    else:
        print(f"[FAIL] {result.get('error', 'Unknown error')}")
        if result.get("pdf_path"):
            print(f"       PDF may exist: {result['pdf_path']}")
        sys.exit(1)


if __name__ == "__main__":
    main()
