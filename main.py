"""Command-line entry point for the reproducible enrichment pipeline."""

from src.letterboxd_analysis.pipeline import run_enrichment


if __name__ == '__main__':
    run_enrichment()
