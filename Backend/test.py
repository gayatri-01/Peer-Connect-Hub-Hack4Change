
import google.generativeai as genai

genai.configure(api_key="AIzaSyABKgZYtF8FUWPyT5QRdXNBeiOlSKluR6k")

model = genai.GenerativeModel('gemini-pro')

# these are basically dropdown questions
input = "Mentor 1 has below qualities as answered in this questionnaire below: \
What describes you the best?=> I am a developer by profession\
Which of the following best describes your current employment status?=> Student, full-time;Employed, part-time\
Which best describes your current work situation?=> Remote\
Which of the following best describes the code you write outside of work?=> Hobby;School or academic work\
Which of the following best describes the highest level of formal education that you've completed?=> Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)\
How do you learn to code?=> Friend or family member;Other online resources (e.g., videos, blogs, forum)\
What online resources do you use to learn to code?=> Formal documentation provided by the owner of the tech;Blogs with tips and tricks;Written Tutorials;Stack Overflow\
What online courses or certifications do you use to learn to code? => nan\
Including any education, how many years have you been coding in total?=> 16\
NOT including education, how many years have you coded professionally (as a part of your work)?=> nan\
Which of the following describes your current job, the one you do most of the time?=> Developer, back-end\
Where do you live?=> Chile\
What languages have you worked with?=> C;C++;JavaScript;Lua;Python;Rust\
What languages are you looking to work with?=> C++;Lua;Python;Rust\
What databases have you worked with?=> PostgreSQL\
What databases are you looking to work with?=> nan\
What platform have you worked on?=> Heroku\
What platform are you looking to work on?=> nan\
What Webframeworks have you worked with?=> FastAPI;React;Ruby on Rails\
What Webframeworks do you want to work with?=> FastAPI;React\
What other Miscellaneous Tech have you worked with?=> NumPy;OpenGL\
What other Miscellaneous Tech do you want to work with?=> OpenGL\
Any other Tools and Technology familiar with?=> APT;Cargo;GNU GCC;Make;npm;Vite\
Any other Tools and Technology you want to get familiar with?=> Cargo\
What collaboration tools have you used?=> Visual Studio Code\
Which other collaboration tools do you wish to use?=> Visual Studio Code\
Are you an individual contributor or people manager?=> nan\
How many years of working experience do you have?=> nan\
Which other professional technologies do you use?=> nan\
What industry is the company you work for in?=> nan\
\
\
Mentor 2 has below qualities as answered in this questionnaire below: \
What describes you the best?=> I am a developer by profession\
Which of the following best describes your current employment status?=> Employed, full-time\
Which best describes your current work situation?=> Remote\
Which of the following best describes the code you write outside of work?=> Contribute to open-source projects\
Which of the following best describes the highest level of formal education that you've completed?=> Associate degree (A.A., A.S., etc.)\
How do you learn to code?=> Colleague;Other online resources (e.g., videos, blogs, forum)\
What online resources do you use to learn to code?=> Formal documentation provided by the owner of the tech;Blogs with tips and tricks;Stack Overflow\
What online courses or certifications do you use to learn to code? => nan\
Including any education, how many years have you been coding in total?=> 15\
NOT including education, how many years have you coded professionally (as a part of your work)?=> 10\
Which of the following describes your current job, the one you do most of the time?=> Developer, back-end\
Where do you live?=> France\
What languages have you worked with?=> Bash/Shell (all shells);Go;JavaScript;PHP;SQL;TypeScript\
What languages are you looking to work with?=> Bash/Shell (all shells);Go;JavaScript;PHP;SQL;TypeScript\
What databases have you worked with?=> BigQuery;MySQL;Redis\
What databases are you looking to work with?=> BigQuery;PostgreSQL;Redis\
What platform have you worked on?=> Google Cloud\
What platform are you looking to work on?=> Google Cloud\
What Webframeworks have you worked with?=> jQuery;Laravel;Node.js;Symfony\
What Webframeworks do you want to work with?=> Symfony\
What other Miscellaneous Tech have you worked with?=> nan\
What other Miscellaneous Tech do you want to work with?=> nan\
Any other Tools and Technology familiar with?=> APT;Composer;Docker;Kubernetes;Make;npm;Terraform;Yarn\
Any other Tools and Technology you want to get familiar with?=> APT;Composer;Docker;Kubernetes;npm;Terraform\
What collaboration tools have you used?=> Goland;PhpStorm;Sublime Text;Vim\
Which other collaboration tools do you wish to use?=> Goland;PhpStorm;Sublime Text;Vim\
Are you an individual contributor or people manager?=> nan\
How many years of working experience do you have?=> nan\
Which other professional technologies do you use?=> nan\
What industry is the company you work for in?=> nan\
\
\
Mentor 3 has below qualities as answered in this questionnaire below: \
What describes you the best?=> I am a developer by profession\
Which of the following best describes your current employment status?=> Employed, full-time\
Which best describes your current work situation?=> Remote\
Which of the following best describes the code you write outside of work?=> I don’t code outside of work\
Which of the following best describes the highest level of formal education that you've completed?=> Associate degree (A.A., A.S., etc.)\
How do you learn to code?=> Books / Physical media;Other online resources (e.g., videos, blogs, forum)\
What online resources do you use to learn to code?=> Formal documentation provided by the owner of the tech;Online challenges (e.g., daily or weekly coding challenges);Stack Overflow\
What online courses or certifications do you use to learn to code? => nan\
Including any education, how many years have you been coding in total?=> 16\
NOT including education, how many years have you coded professionally (as a part of your work)?=> 10\
Which of the following describes your current job, the one you do most of the time?=> Developer, back-end\
Where do you live?=> United Kingdom of Great Britain and Northern Ireland\
What languages have you worked with?=> Bash/Shell (all shells);Rust;TypeScript\
What languages are you looking to work with?=> nan\
What databases have you worked with?=> Dynamodb;Elasticsearch;PostgreSQL;Redis\
What databases are you looking to work with?=> nan\
What platform have you worked on?=> Amazon Web Services (AWS);Google Cloud\
What platform are you looking to work on?=> nan\
What Webframeworks have you worked with?=> Express\
What Webframeworks do you want to work with?=> nan\
What other Miscellaneous Tech have you worked with?=> nan\
What other Miscellaneous Tech do you want to work with?=> nan\
Any other Tools and Technology familiar with?=> Docker;pnpm;Terraform\
Any other Tools and Technology you want to get familiar with?=> nan\
What collaboration tools have you used?=> Neovim\
Which other collaboration tools do you wish to use?=> nan\
Are you an individual contributor or people manager?=> nan\
How many years of working experience do you have?=> nan\
Which other professional technologies do you use?=> nan\
What industry is the company you work for in?=> nan\
\
\
My qualities are as shared in the questionnaire below :\
What describes you the best?=> I am a developer by profession\
Which of the following best describes your current employment status?=> Employed, full-time\
Which best describes your current work situation?=> Remote\
Which of the following best describes the code you write outside of work?=> Hobby;Contribute to open-source projects;Bootstrapping a business;Professional development or self-paced learning from online courses;Freelance/contract work\
Which of the following best describes the highest level of formal education that you've completed?=> Master’s degree (M.A., M.S., M.Eng., MBA, etc.)\
How do you learn to code?=> Books / Physical media;Online Courses or Certification;On the job training;School (i.e., University, College, etc)\
What online resources do you use to learn to code?=> nan\
What online courses or certifications do you use to learn to code? => Udemy;Pluralsight;Coursera\
Including any education, how many years have you been coding in total?=> 12\
NOT including education, how many years have you coded professionally (as a part of your work)?=> 10\
Which of the following describes your current job, the one you do most of the time?=> Cloud infrastructure engineer\
Where do you live?=> United States of America\
What languages have you worked with?=> HTML/CSS;Java;PHP;Python;R;SQL;TypeScript\
What languages are you looking to work with?=> MATLAB;OCaml;Scala\
What databases have you worked with?=> Dynamodb;IBM DB2;Microsoft SQL Server;MongoDB;MySQL;Oracle;PostgreSQL;Solr;SQLite\
What databases are you looking to work with?=> Redis;Snowflake\
What platform have you worked on?=> Amazon Web Services (AWS);Google Cloud;Microsoft Azure\
What platform are you looking to work on?=> IBM Cloud Or Watson;OpenShift;OpenStack\
What Webframeworks have you worked with?=> Angular;ASP.NET;Deno;Django;Drupal;FastAPI;jQuery;Node.js;Nuxt.js;Spring Boot;Symfony;Vue.js;WordPress\
What Webframeworks do you want to work with?=> Blazor;Phoenix;React\
What other Miscellaneous Tech have you worked with?=> Flutter;Ionic;Opencv;RabbitMQ;Spring Framework;SwiftUI\
What other Miscellaneous Tech do you want to work with?=> Apache Kafka;Apache Spark;Pandas;Quarkus;TensorFlow\
Any other Tools and Technology familiar with?=> Ansible;Chocolatey;Composer;Docker;Google Test;Homebrew;Kubernetes;Make;Nix;npm;Pip;Podman;Puppet;Terraform\
Any other Tools and Technology you want to get familiar with?=> Unreal Engine;Yarn\
What collaboration tools have you used?=> Eclipse;IntelliJ IDEA;Neovim;Notepad++;PhpStorm;RStudio;Sublime Text;Vim;Visual Studio;Visual Studio Code;VSCodium;Xcode\
Which other collaboration tools do you wish to use?=> nan\
Are you an individual contributor or people manager?=> People manager\
How many years of working experience do you have?=> 12.0\
Which other professional technologies do you use?=> DevOps function;Microservices;Automated testing;Observability tools;Continuous integration (CI) and (more often) continuous delivery\
What industry is the company you work for in?=> Information Services, IT, Software Development, or other Technology\
\
Explain elaborately how each of these 3 mentors will be a good match for me\
"


response = model.generate_content(input)
print(response.text) 