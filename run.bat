echo "Creating variables: "
set FLASK_APP=main 
set FLASK_ENV=development

source venv/bin/activate 

cd app 

flask run 
