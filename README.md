# cookiecutter-mvtec
Cookiecutter Template for Unsupervised Anomaly Detection on MVTec AD Dataset

<br>

## Usage

a) Create RIAD directory
```
$ cookiecutter https://github.com/taikiinoue45/cookiecutter-mvtec/
upper_project_name [MVTec]: RIAD
lower_project_name [mvtec]: riad
```

b) Add a remote and push it to Github
```
cd RIAD
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin git@github.com:taikiinoue45/RIAD.git
git push -u origin main
```
