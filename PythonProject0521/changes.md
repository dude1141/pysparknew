# Changes

---

## v1.1.0 — 2026-05-21

| # | What was wrong | Fix |
|---|---|---|
| 1 | Running `pipeline.py` directly in PyCharm showed `Process finished with exit code 0` with no output — `pipeline.py` had no `if __name__ == "__main__":` block so it just defined the class and exited | Added `if __name__ == "__main__":` block in `pipeline.py` that loads `config/dev.yaml` and calls `Pipeline(config).execute()` |
| 2 | `from src.reader import read_data` threw `ModuleNotFoundError` when running `pipeline.py` directly because the project root was not in `sys.path` | Added `sys.path.insert(0, ...)` at the top of `pipeline.py` pointing to the project root so all `src.*` imports resolve correctly |
| 3 | No transformed data was visible in the console — only row counts were printed — so there was no way to verify dedup, uppercase, and salary filter were working | Added `df.show(truncate=False)` after reading raw data and again after transformations so both before and after rows are printed |
| 4 | `load_config` was not imported in `pipeline.py` so the `__main__` block had no way to load the YAML config | Added `from src.utils import load_config` import in `pipeline.py` |

---

## v1.0.0 — 2026-05-21

| # | What was wrong | Fix |
|---|---|---|
| 1 | No project structure existed — only pseudocode notes in `may21_yaml_approach1.txt` with syntax errors and no runnable files | Created full project from scratch based on the notes and the [spark-etl](https://github.com/naveenkumarbaskaran/spark-etl) reference repo |
| 2 | Config approach in notes used plain dictionaries — not scalable for dev/prod environments | Created `config/dev.yaml` and `config/prod.yaml` with environment-specific settings (shuffle partitions, log level, output path) |
| 3 | `reader.py` pseudocode had no class structure and mixed up Spark read options incorrectly | Created `CSVSource` class extending abstract `Source` with correct PySpark `.read.format().option().load()` chain |
| 4 | `transformer.py` pseudocode had broken indentation, wrong method names (`dropduplicates` instead of `dropDuplicates`), and missing imports | Created `transformer.py` with correct PySpark function imports (`col`, `upper`) and properly chained `drop_duplicates`, `uppercase_columns`, `filter_salary` |
| 5 | `writer.py` pseudocode had syntax error `Save.(config[...])` and no class structure | Created `ParquetSink` class with correct `.write.mode().parquet()` call |
| 6 | `main.py` pseudocode had no CLI, hardcoded config path, and wrong class names (`sparksession`, `SparkSesion`) | Created `__main__.py` with Click CLI supporting `run` (with `--dry-run`) and `validate` commands |
