pipeline {

	agent any 
	
	environment {
		FRONTEND_DOCKER_IMAGE_NAME = 'frontend'
        BACKEND_DOCKER_IMAGE_NAME = 'backend'
		GITHUB_REPO_URL = 'https://github.com/hemantkumarc/SoftwareProductionEngineeringMajor.git'
	}

	stages {
		
		stage('Clone Project')
		{
			steps {

				script{
					git branch: 'main', url: "${GITHUB_REPO_URL}"
				}

			}
		}

        stage('Test Code')
		{
			steps {
				echo "Testing the code"
			}
		}

		stage('Build Code')
		{
			steps {
				echo "Building the code"
			}
		}

		stage('Building Docker Images')
		{
			steps {

				script {
                    sh "cd /frontend"
					docker.build("${FRONTEND_DOCKER_IMAGE_NAME}", '.')
                    sh "docker image tag ${FRONTEND_DOCKER_IMAGE_NAME} hemantkumarcpersonal/${FRONTEND_DOCKER_IMAGE_NAME}:latest"
                    
                    sh "cd /backend"
                    docker.build("${BACKEND_DOCKER_IMAGE_NAME}", '.')
                    sh "docker image tag ${BACKEND_DOCKER_IMAGE_NAME} hemantkumarcpersonal/${BACKEND_DOCKER_IMAGE_NAME}:latest"
				}
			}
		}

		stage('Pushing Docker Images')
		{
			steps {

				script {

					docker.withRegistry('', 'dockerhub-credentials') {
						// sh "docker image tag calculator hemantkumarcpersonal/calculator:latest"
						sh "docker push hemantkumarcpersonal/${FRONTEND_DOCKER_IMAGE_NAME}:latest"
                        sh "docker push hemantkumarcpersonal/${BACKEND_DOCKER_IMAGE_NAME}:latest"
					}
				}

			}
		}

		stage('Run Ansible Playbook')
		{
			steps {

				script {

					ansiblePlaybook (

						playbook: 'playbook.yml',
						inventory: 'inventory.ini'
					)
				}
			}
		}
	}
}