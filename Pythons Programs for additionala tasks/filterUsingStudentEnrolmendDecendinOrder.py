from sqlalchemy import create_engine
import pandas as pd

# Replace with your actual MySQL database information
DATABASE_URI = "mysql+mysqlconnector://root:@localhost/course_details"

# Create a SQLAlchemy engine to connect to the MySQL database
engine = create_engine(DATABASE_URI)

# Replace 'your_table_name' with the actual table name where your data is stored
table_name = 'course_details'

# Write a SQL query to get courses with students enrolled in descending order
query = f"SELECT course_title FROM {table_name} ORDER BY CAST(course_students_enrolled AS SIGNED) DESC"

# Execute the query and fetch the results into a pandas DataFrame
df = pd.read_sql_query(query, engine)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Display the result
print(df)

# Dispose of the engine
engine.dispose()


'''Output

                                          course_title
0               Modern and Contemporary Art and Design
1            Improve Your English Communication Skills
2                                       Career Success
3                    Data Science: Foundations using R
4                                        Deep Learning
5                                Chinese for Beginners
6                                    Financial Markets
7                            Academic English: Writing
8                                     IBM Data Science
9                     Applied Data Science with Python
10                              Python Data Structures
11                                   Google IT Support
12                                   First Step Korean
13   Speak English Professionally: In Person, Onlin...
14                                Business Foundations
15   Project Management & Other Tools for Career De...
16    Excel to MySQL: Analytic Techniques for Business
17                                       R Programming
18                        The Data Scientist’s Toolbox
19                                     AI For Everyone
20              Introduction to Data Science in Python
21   Java Programming and Software Engineering Fund...
22                                   Digital Marketing
23                      Technical Support Fundamentals
24                           Excel Skills for Business
25                                      Graphic Design
26           SRE and DevOps Engineer with Google Cloud
27                          Introduction to Psychology
28            Stanford Introduction to Food and Health
29                          Introduction to Philosophy
30                       Key Technologies for Business
31                     IBM AI Foundations for Business
32                     Using Python to Access Web Data
33                Cloud Architecture with Google Cloud
34             Architecting with Google Compute Engine
35                 Cloud Engineering with Google Cloud
36                        Introduction to Data Science
37   Developing Applications with Google Cloud Plat...
38   Web Design for Everybody: Basics of Web Develo...
39                      Data Structures and Algorithms
40                 Object Oriented Programming in Java
41               Excel Skills for Business: Essentials
42                        Marketing in a Digital World
43          Architecting with Google Kubernetes Engine
44                   Security in Google Cloud Platform
45                          Networking in Google Cloud
46   Google Cloud Platform Fundamentals: Core Infra...
47                         Child Nutrition and Cooking
48        HTML, CSS, and Javascript for Web Developers
49                                    Machine Learning
50                          Seeing Through Photographs
51        Competitive Strategy and Organization Design
52                               The Singer Songwriter
53     MATLAB Programming for Engineers and Scientists
54   An Introduction to Programming the Internet of...
55                                  Modern Art & Ideas
56                                 Finanzas personales
57                                    IBM Data Analyst
58                               What is Data Science?
59    Financial Engineering and Risk Management Part I
60   Improving Deep Neural Networks: Hyperparameter...
61                               Introduction to HTML5
62   Programming Foundations with JavaScript, HTML ...
63                                      IBM Applied AI
64              Introduction to Finance and Accounting
65                                   Social Psychology
66         Project Management Principles and Practices
67                       Introductory Human Physiology
68                         Using Databases with Python
69                                 Algorithmic Toolbox
70                                  Business Analytics
71           Methods and Statistics in Social Sciences
72                       Convolutional Neural Networks
73   Machine Learning Foundations: A Case Study App...
74                          Introduction to Psychology
75               Introduction to Mathematical Thinking
76                      Design Thinking for Innovation
77   Mindshift: Break Through Obstacles to Learning...
78                                Applied Data Science
79        Finance & Quantitative Modeling for Analysts
80                                         Game Theory
81   Object Oriented Java Programming: Data Structu...
82                     Contabilidad para no contadores
83                             Psychological First Aid
84                      Coding for Everyone: C and C++
85                                      Cryptography I
86                                   Statistics with R
87                            Leading People and Teams
88                                            Big Data
89                           Advanced Machine Learning
90                    Initiating and Planning Projects
91           English for Business and Entrepreneurship
92         Introduction to Logic and Critical Thinking
93                                  How to Play Guitar
94                    Google IT Automation with Python
95                   Learn SQL Basics for Data Science
96                           Introduction to Marketing
97       Data Science: Statistics and Machine Learning
98   Étudier en France: French Intermediate course ...
99                               English Composition I
100               DeepLearning.AI TensorFlow Developer
101  Data Analysis and Presentation Skills: the PwC...
102              Full-Stack Web Development with React
103                               SQL for Data Science
104                               Guitar for Beginners
105         Think Again I: How to Understand Arguments
106  Aprendiendo a aprender: Poderosas herramientas...
107                               Python 3 Programming
108                    Functional Programming in Scala
109     Camino a la Excelencia en Gestión de Proyectos
110                                Marketing Analytics
111                     Python for Data Science and AI
112                          Fundamentals of Computing
113               Introduction to Financial Accounting
114  Vital Signs: Understanding What the Body Is Te...
115                                  Fashion as Design
116                                Positive Psychology
117   Java Programming: Solving Problems with Software
118                           Introduction to Big Data
119          The Bits and Bytes of Computer Networking
120                             Crash Course on Python
121                                   AWS Fundamentals
122            Entrepreneurship: Growing Your Business
123  Photography Basics and Beyond: From Smartphone...
124  Introduction to TensorFlow for Artificial Inte...
125                           Data Science Math Skills
126                                Science of Exercise
127          Responsive Website Development and Design
128                 Learn to Program: The Fundamentals
129                       Fundamentals of Music Theory
130                         Digital Product Management
131   Mathematics for Machine Learning: Linear Algebra
132                               Medical Neuroscience
133         Business Metrics for Data-Driven Companies
134  The Power of Macroeconomics: Economic Principl...
135        Introduction to Probability and Data with R
136                 Fundamentos de Excel para Negocios
137                                   Basic Statistics
138                 Applied Machine Learning in Python
139                     Web Applications for Everybody
140                             Executive Data Science
141                                 Customer Analytics
142               AWS Fundamentals: Going Cloud-Native
143                            Learn to Speak Korean 1
144        How Things Work: An Introduction to Physics
145                    Business and Financial Modeling
146                                 IBM AI Engineering
147                   Search Engine Optimization (SEO)
148                            Writing in the Sciences
149  Viral Marketing and How to Craft Contagious Co...
150           Business English for Non-Native Speakers
151             Gestión Empresarial Exitosa para Pymes
152                          De-Mystifying Mindfulness
.
.
rest of courses
'''