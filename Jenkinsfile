pipeline {
  agent any
  stages {
    stage('SCM') {
      steps {
        git(url: 'git@github.com:lordoftheflies/gargantula.git', branch: 'master', changelog: true, credentialsId: 'credentials-github-lordoftheflies-ssh', poll: true)
      }
    }
    stage('Install virtual environment') {
      steps {
        sh '''if [ ! -d "env" ]; then
    virtualenv --no-site-packages -p /usr/bin/python3.4 env
fi
'''
      }
    }
    stage('Setup dotenv') {
      steps {
        sh '''if [ ! -f "scrapersite/.env" ]; then
    cp env.template scrapersite/.env
    sed -i -- 's/DEVELOPMENT/STAGING/g' scrapersite/.env
fi
'''
        sh '''if [ ! -f "portalcrawler/.env" ]; then
    cp env.template portalcrawler/.env
    sed -i -- 's/DEVELOPMENT/STAGING/g' portalcrawler/.env
fi
'''
      }
    }
    stage('Setup') {
      steps {
        parallel(
          "Setup crawler": {
            sh '''. ./env/bin/activate
pip install -r portalcrawler/requirements.txt
deactivate
'''
            
          },
          "Setup site": {
            sh '''. ./env/bin/activate
pip install -r scrapersite/requirements.txt --extra-index-url=https://pypi.cherubits.hu
python scrapersite/manage.py collectstatic --noinput
python scrapersite/manage.py migrate
deactivate
'''
            
          }
        )
      }
    }
    stage('Build') {
      steps {
        parallel(
          "Build crawler": {
            sh '''. ./env/bin/activate
python portalcrawler/setup.py sdist develop
deactivate
'''
            
          },
          "Build site": {
            sh '''. ./env/bin/activate
python scrapersite/setup.py sdist develop
deactivate
'''
            
          }
        )
      }
    }
    stage('Test') {
      steps {
        parallel(
          "Test crawler": {
            sh '''. ./env/bin/activate
python -m unittest discover portalcrawler/tests/ -p '*_test.py'
deactivate
'''
            
          },
          "Test site": {
            sh '''. ./env/bin/activate
cd scrapersite
deactivate
'''
            
          }
        )
      }
    }
    stage('Deploy staging') {
      steps {
        parallel(
          "Deploy crawler": {
            sh '''. ./env/bin/activate
python portalcrawler/setup.py sdist install
deactivate
'''
            
          },
          "Deploy site": {
            sh '''. ./env/bin/activate
python scrapersite/setup.py sdist install
deactivate
'''
            
          }
        )
      }
    }
    stage('Update version') {
      steps {
        sh '''. ./env/bin/activate
GARGANTULA_PORTALCRAWLER_VERSION=$(cat portalcrawler/portalcrawler/version.py | grep "__version__ = " | sed 's/__version__ =//' | tr -d "'")
echo "$GARGANTULA_PORTALCRAWLER_VERSION"
bumpversion --allow-dirty --message 'Jenkins Build {$BUILD_NUMBER} bump version of portalcrawler: {current_version} -> {new_version}' --commit --current-version $GARGANTULA_PORTALCRAWLER_VERSION patch portalcrawler/scrapy.cfg portalcrawler/portalcrawler/version.py
deactivate
'''
        sh '''. ./env/bin/activate
GARGANTULA_SCRAPERSITE_VERSION=$(cat scrapersite/scrapersite/version.py | grep "__version__ = " | sed 's/__version__ =//' | tr -d "'")
echo "$GARGANTULA_SCRAPERSITE_VERSION"
bumpversion --allow-dirty --message 'Jenkins Build {$BUILD_NUMBER} bump version of scrapersite: {current_version} -> {new_version}' --commit --current-version $GARGANTULA_SCRAPERSITE_VERSION patch scrapersite/scrapersite/version.py
deactivate
'''
        sh '''git push origin master
'''
      }
    }
    stage('Distribute') {
      steps {
        sh '''. ./env/bin/activate
python scrapersite/setup.py sdist upload -r local
python portalcrawler/setup.py sdist upload -r local
deactivate
'''
        catchError() {
          echo 'Distritbution failed.'
        }
        
      }
    }
    stage('Deploy production') {
      steps {
        sh '''cd ./ansible
ansible-playbook ./update.playbook.yml --extra-vars "ansible_become_pass=Armageddon0"
'''
      }
    }
  }
}