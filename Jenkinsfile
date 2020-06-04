pipeline {
   agent  {
      node {
        label 'docker'
      }
   }

   environment {
       registry = "nexus.local.net:8123"
       registryurl = "http://nexus.local.net:8123"
       def BUILDTIME = sh(script: "echo `date +%Y%m%d-%H%M`", returnStdout: true).trim()
   }
   stages {
       stage('Cleanup workspace and checkout scm') {
           steps {
               cleanWs()
               checkout scm
           }
       }
       stage('Build docker image based on updated code') {
           steps {
              echo 'Starting to build docker image'
              script {
                env.appImage = env.registry + "/django-blog:${env.BUILDTIME}"
                buildImage = docker.build("${env.registry}" + "/django-blog:${env.BUILDTIME}")
              }
           }
       }
       stage('Integration test') {
           steps {
               script {
                  sh '''
                  cd test
                  set -a
                  docker-compose config
                  docker-compose -p blog up --abort-on-container-exit --exit-code-from curl
                  docker-compose -p blog rm -f
                  '''
              }
           }
       }
       stage('Publish docker image to nexus repo') {
           steps{
               script {
                   docker.withRegistry( registryurl, 'nexus' ) {
                      buildImage.push()
                      buildImage.push('latest')
                   }
               }
           }
       }
        stage('Aprove deployment step') {
            steps {
                script {
                    def deploymentDelay = input id: 'Deploy', message: 'Deploy to production?', submitter: 'adrian', 
                    parameters: [choice(choices: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'], 
                    description: 'Hours to delay deployment?', name: 'deploymentDelay')]
                    sleep time: deploymentDelay.toInteger(), unit: 'HOURS'
                }
            }
        }
       stage ('Deploy to Kubernetes cluster') {
           steps {
               script{
                  withCredentials([kubeconfigFile(credentialsId: 'k8smaster', variable: 'KUBECONFIG')]){
                     ansiColor('xterm') {
                       ansiblePlaybook (
                       colorized: true,
                       playbook: 'deploy/playbook.yml',
                       extras: "-e \"appImage=${appImage}\" -vv")
                     }
                  }
               }
           }
       }
    }
    post { 
        success {  
            echo 'Deployment-ul s-a efectuat cu succes'
            echo 'Pornesc testarea functionala'
            emailext (
            subject: "Deployment-ul aplicatiei pe mediul Kubernetes are status: ${currentBuild.currentResult}: Job ${env.JOB_NAME}",
            body: 'Deployment-ul aplicatiei my-blog pe mediul Kubernetes: ${currentBuild.currentResult}: Job ${env.JOB_NAME}',
            to: adrianiacob22@gmail.com)
            build job: 'Testare_automata'
        }
        failure {
            emailext (
            subject: "Deployment-ul aplicatiei pe mediul Kubernetes are status: ${currentBuild.currentResult}: Job ${env.JOB_NAME}",
            body: 'Deployment-ul aplicatiei my-blog pe mediul Kubernetes: ${currentBuild.currentResult}: Job ${env.JOB_NAME}',
            to: adrianiacob22@gmail.com)
        }
        changed {
            emailext (
            subject: "Deployment-ul aplicatiei pe mediul Kubernetes are status: ${currentBuild.currentResult}: Job ${env.JOB_NAME}",
            body: 'Deployment-ul aplicatiei my-blog pe mediul Kubernetes: ${currentBuild.currentResult}: Job ${env.JOB_NAME}',
            to: adrianiacob22@gmail.com)
        } 
    }
}
