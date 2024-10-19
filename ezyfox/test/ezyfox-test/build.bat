:: set EZYFOX_SERVER_HOME=
mvn -pl . clean install & ^
mvn -pl ezyfox-test-common -Pexport clean install & ^
mvn -pl ezyfox-test-app-api -Pexport clean install & ^
mvn -pl ezyfox-test-app-entry -Pexport clean install & ^
mvn -pl ezyfox-test-plugin -Pexport clean install & ^
copy ezyfox-test-zone-settings.xml %EZYFOX_SERVER_HOME%/settings/zones/
