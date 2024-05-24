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
                    sh "cd ./frontend"
					docker.build("${FRONTEND_DOCKER_IMAGE_NAME}", 'frontend')
                    sh "docker image tag ${FRONTEND_DOCKER_IMAGE_NAME} hemantkumarcpersonal/${FRONTEND_DOCKER_IMAGE_NAME}:latest"
                    
                    docker.build("${BACKEND_DOCKER_IMAGE_NAME}", 'backend')
                    sh "docker image tag ${BACKEND_DOCKER_IMAGE_NAME} hemantkumarcpersonal/${BACKEND_DOCKER_IMAGE_NAME}:latest"
				}
			}
		}

		stage('Pushing Docker Images')
		{
			steps {

				script {
					docker.withRegistry('', 'dockerhub-credentials') {
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
						inventory: 'inventory.ini',
                        colorized: true
					)

                    // withCredentials([file(credentialsId: 'gcp-service-account-file', variable: 'GCP_CREDENTIALS')]) {
                    //     // env.GOOGLE_APPLICATION_CREDENTIALS = GCP_CREDENTIALSs
                    //     ansiblePlaybook(
                    //         playbook: 'playbook.yml',
                    //         inventory: 'inventory.ini',
                    //         extraVars: [
                    //             "service_account_file=${GCP_CREDENTIALS}",
                    //             // "kubeconfig=${KUBECONFIG_FILE}"
                    //         ]
                    //     )
                    // }
				}
			}
		}
	}
}