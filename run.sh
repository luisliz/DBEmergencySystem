echo "Creating variables: "
export FLASK_APP=main 
export FLASK_ENV=development

source venv/bin/activate 

cd app 

flask run 
