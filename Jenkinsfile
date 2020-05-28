pipeline {
   agent  {
      node {
            label 'docker'
      }
   }

   environment {
       registry = "nexus.local.net:8123"
       registryurl = "http://nexus.local.net:8123"
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
                env.appImage = env.registry + "/django-blog:${env.BUILD_ID}"
                buildImage = docker.build("${env.registry}" + "/django-blog:${env.BUILD_ID}")
              }
           }
       }
       stage('Integration test') {
           steps {
               script {
                  sh '''
                  cd test
                  set -a
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
}
