# spark_on_k8s_gcp

Pyspark pipeline executing inside a Kubernetes cluster. It contains:
  - Docker file for the spark application
  - conf files to access GCS bucket
  - jars to access GCS
  - yamls for setting up ClusterRoleBinding and executing the spark application

This repository contains the files used in a medium tutorial. You can check out using this link:
https://medium.com/@contatocesarino/running-a-spark-job-using-spark-on-k8s-operator-12e5c8336fa8
