# Databricks notebook source
import sys
sys.path.append("/Workspace/Projects/jason.kim@databricks.com/test")

# COMMAND ----------

import foo

# COMMAND ----------

from pathlib import Path

print(Path("/Workspace/Projects/jason.kim@databricks.com/test/data.csv").read_text())

# COMMAND ----------

