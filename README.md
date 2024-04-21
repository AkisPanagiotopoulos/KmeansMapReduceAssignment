# KmeansMapReduceAssignment

1) Run the points_dataset_creation.py to get one million points (dataset.txt) biased toward the creation of three clusters which are located in the created (centroids.txt).The starting centroids for the creation of the points are predeffined.

2) For this assignment i worked on a cloudera distibution in virtualbox. The next step is to move the mapper.py and reducer.py to hdfs as well as centroids.txt and dataset.txt files in hdfs data directory that we have created with the commands:

```bash
hdfs dfs -put mapper.py reducer.py /user/cloudera
hdfs dfs -put dataset.txt /user/cloudera/data
hdfs dfs -put centroids.txt /user/cloudera/data
```

3) Then we run the command:

```bash
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar     -files hdfs://quickstart.cloudera:8020/user/cloudera/data/centroids.txt,hdfs://quickstart.cloudera:8020/user/cloudera/mapper.py,hdfs://quickstart.cloudera:8020/user/cloudera/reducer.py     -mapper 'python mapper.py'     -reducer 'python reducer.py'     -input hdfs://quickstart.cloudera:8020/user/cloudera/data/dataset.txt     -output hdfs://quickstart.cloudera:8020/user/cloudera/output
```

to invoke Hadoop's streaming job using the provided JAR file (hadoop-streaming.jar). It specifies the Python mapper (mapper.py) and reducer (reducer.py) scripts located in HDFS (hdfs://quickstart.cloudera:8020/user/cloudera/). The mapper and reducer scripts are executed using Python. The input data (dataset.txt) is read from HDFS, and the output is stored in the specified directory (output) in HDFS. Essentially, it runs a MapReduce job using the provided Python scripts on the given input data.
