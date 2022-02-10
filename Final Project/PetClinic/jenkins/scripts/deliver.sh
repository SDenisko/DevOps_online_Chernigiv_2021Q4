#!/usr/bin/env bash

echo 'The following Maven command installs your Maven-built Java application'
echo 'into the local Maven repository, which will ultimately be stored in'
echo 'Jenkins''s local Maven repository (and the "maven-repository" Docker data'
echo 'volume).'
set -x
mvn jar:jar install:install help:evaluate -Dexpression=project.name

set +x

echo 'The following complex command extracts the value of the <name/> element'
echo 'within <project/> of your Java/Maven project''s "pom.xml" file.'
set -x
NAME=`mvn help:evaluate -Dexpression=project.name | grep "^[^\[]"`
set +x

echo 'The following complex command behaves similarly to the previous one but'
echo 'extracts the value of the <version/> element within <project/> instead.'
set -x
VERSION=`mvn help:evaluate -Dexpression=project.version | grep "^[^\[]"`
set +x
#pwd
#mkdir /tmp/petclinic_www
#ppp=`ls /tmp | grep petclinic_www`
cp /var/lib/jenkins/workspace/petClinic/target/spring-*.jar /var/lib/jenkins/workspace/petClinic/
#cd /var/lib/jenkins/workspace/petClinic/
#docker build -t sioj/petclinic:1.0-SHAPSHOT .
#java -jar /home/mrbit/petclinic/${NAME}-${VERSION}.jar
#echo 'The following command runs and outputs the execution of your Java'
#echo 'application (which Jenkins built using Maven) to the Jenkins UI.'
#set -x
#java -jar /tmp/spring-${NAME}-${VERSION}.jar
