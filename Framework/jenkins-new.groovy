pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout your source code from the repository
                checkout scm
            }
        }
        
        stage('Build and Test') {
            steps {
                // Build and test your Robot Framework code
                sh 'C:/Users/Kamal Teja INT-212/PycharmProjects/Myproject/Framework'
            }
        }
        
        stage('Deploy to Test Environment') {
            when {
                // Define when to deploy, e.g., after a successful build and test stage
                expression { currentBuild.resultIsBetterOrEqualTo('SUCCESS') }
            }
            steps {
                // Deploy to your test environment here
                sh 'ansible-playbook deploy_test.yml'  // Example using Ansible
            }
        }
        
        stage('Deploy to Production Environment') {
            when {
                // Define when to deploy to production, e.g., manual approval or after successful test deployment
                input message: 'Deploy to production?', ok: 'Deploy'
            }
            steps {
                // Deploy to your production environment here
                sh 'ansible-playbook deploy_production.yml'  // Example using Ansible
            }
        }
    }
    
    post {
        always {
            // Perform cleanup or other actions after deployment
        }
    }
}
