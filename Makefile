run:
	@streamlit run streamlit_app.py --server.port=8080 --server.address=0.0.0.0

run-container:
	@docker build . -t $APP_NAME
	@docker run -p 8081:8081 $APP_NAME

gcloud-deploy:
	@gcloud app deploy app.yaml
