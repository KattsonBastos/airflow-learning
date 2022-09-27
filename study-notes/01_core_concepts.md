# Airflow: walking through some core concepts<p id="core_concepts"></p>

<a href="https://github.com/KattsonBastos/ml-with-airflow#contents">Back to Contents</a>

## What Airflow is?<p id="a1"></p>
<p align="justify">
&ensp;&ensp;&ensp;&ensp;In simply put, Airflow is a job scheduler with some extra powers. That 'job' can be anything, not only data related jobs.
</p>

<p align="justify">
&ensp;&ensp;&ensp;&ensp;But let's see a more formal definition. According to <a href="https://airflow.apache.org/docs/apache-airflow/stable/index.html">the documentation</a>, it is a platform (and open-source) used for workflow's development, scheduling, and monitoring. In addition, it allows us to build workflows connected with many other technologies, such as container's orchestrators and cloud services.
</p>

<p align="justify">
&ensp;&ensp;&ensp;&ensp;Since Airflow is developed in Python (and the workflow we build with it too), it is chosen by many professionals since Python brings a lot of extensibility and scalability to our application. Although that python-based characteristic is usually taken as an advantage, it can also be a disadvantage: it requires the developer to know Python Programming.
</p>

<p align="justify">
&ensp;&ensp;&ensp;&ensp;Besides that, Airflow brings, among many others, a lot more facilities:
</p>

- A friendly UI for monitoring all scheduled/executed/running tasks;

- Integration with a lot of other tools;

- Backfilling for processing, for running dags for a specified historical period;
- A lot of scheduling options;

- CI/CD pipelines implementations;

- It is already integrated in the largest cloud providers.

<p align="justify">
&ensp;&ensp;&ensp;&ensp;It is important to note that Airflow is not recommended for streaming pipelines. <a href="https://airflow.apache.org/docs/apache-airflow/stable/index.html">The documentation</a> explicitly says that it is built for "batch-oriented workflows". Also, the workflows are "expected to be mostly static or slowly changing."

</p>

<br>

## What is a DAG?<p id="a2"></p>

<p align="justify">
&ensp;&ensp;&ensp;&ensp;The word <strong>DAG</strong> means <strong>Directed Acyclic Graph</strong>. It is basically a collection of all tasks (the workflow) defined as a graph, as shows the following image:
</p>

<img src="../images/training_dag.png" alt="drawing" width="100%"/>

<p align="justify">
&ensp;&ensp;&ensp;&ensp; The above image shows a DAG for a very simple Machine Learning pipeline. There's a direct dependency between all the nodes/tasks (that's the way Airflow works). Also, the flow is not cyclic, that is, once it passed through a task, it won't go back in the same execution.
</p>

<p align="justify">
&ensp;&ensp;&ensp;&ensp;The idea of a DAG is to wrap up all of our tasks, the relationship between them, and their depencencies. Based on the later image, our example DAG has six tasks, where the Data Processing dependends on the success of the Data Loading; the models only will be trained if the data is processed (success on Data Processing); and they'll be evaluated only if the three model training tasks have a success.
</p>

<p align="justify">
&ensp;&ensp;&ensp;&ensp;The good thing here is that Airflow allows us to customize all of that dependencies and relationships.
</p>


## Underlying Components<p id="a3"></p>

<img src="../images/components.png" alt="drawing" width="100%"/>

<br>

- **Scheduler**: submit tasks to the executor to run. It also triggers scheduled workflows;

- **Executor**: the components that actually run the tasks. This Executor runs taks both inside the scheduler (in the default Airflow installation) or inside external workers. Executors can be: Sequential, Local, Celery, Dask, Kubernetes;

- **Workers**: a processor/service/container which runs a task at once;

- **Webserver**: a Flask server that presents a UI to inspect, trigger and debug the both the DAGs and the Tasks

- **DAG Files Storage**: a directory or database where are stored all the python files that contains the dags;

- **Metadata Storage**: use to store states by the scheduler, executors and the UI server.


## Tasks and Operators<p id="a4"></p>

<p align="justify">
&ensp;&ensp;&ensp;&ensp;Airflow's Operators define what is going to be executed: a bash command, a python function, a SQL query, among many others. For each task we want to run in our pipeline, we instantiate an Operator.
</p>

<p align="justify">
&ensp;&ensp;&ensp;&ensp;In this way, an <strong>Operator</strong> is a Python class; a <strong>Task</strong> is an instantiated Operator with the required parameters adn dependencies.
</p>

<p align="justify">
&ensp;&ensp;&ensp;&ensp;Airflow has an abstract base operator class (<a href="https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/models/baseoperator/index.html">BaseOperator</a>, a "Base operator for all operators", as says the documentation) in which all the other operators inherit from it. That class makes Airflow a lot more powerful because it allows us to create our own operators to suit our needs.
</p>

<p align="justify">
&ensp;&ensp;&ensp;&ensp;Even though we can create custom operators, we already have some popular ones integrated in Airflow:
</p>



<img src="../images/operators.png" alt="drawing" width="100%"/>

- **BashOperator**: executes both Bash *scripts*, *commands* or a *set of commands*;

- **PythonOperator**: executes Python callables, that is, *function-like objects*;

- **MySqlOperator**: executes *SQl queries* in a given MySQL database;

- **DockerOperator**: executes commands inside a Docker container.

Besides that, Airflow also has operators for all the major cloud providers. For example, there're the following for AWS (among others):

- **S3CreateBucketOperator**, **S3DeleteBucketOperator**: to create/delete specified S3 buckets;

- **EC2StartInstanceOperator**: starts specified EC2 instances;

