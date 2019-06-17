gem install travis -v 1.8.10;

travis login --org --github-token "$SANTE_GH_TOKEN";

body='{
"request": {
"message": "Triggered by '$TRAVIS_COMMIT_MESSAGE' in django-accelerator",
"branch":"'$TRAVIS_BRANCH'",
"config": {
"script": "echo \"The tests dont need to run.\""
}
}}'

curl -s -X POST \
-H "Content-Type:application/json" \
-H "Accept:application/json" \
-H "Travis-API-Version:3" \
-H "Authorization:token $(travis token --org)" \
-d "$body" \
https://api.travis-ci.org/repo/masschallenge%2Fimpact-api/requests;

printenv