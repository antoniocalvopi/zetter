#!/bin/bash
declare -A technologies
technologies=(
    ["Django"]="https://www.djangoproject.com/"
    ["Django Rest Framework"]="https://www.django-rest-framework.org/"
    ["JWT (JSON Web Tokens)"]="https://jwt.io/"
    ["PostgreSQL"]="https://www.postgresql.org/"
    ["Docker"]="https://www.docker.com/"
    ["Celery"]="https://docs.celeryproject.org/en/stable/"
    ["Redis"]="https://redis.io/"
    ["Nginx"]="https://www.nginx.com/"
    ["Gunicorn"]="https://gunicorn.org/"
    ["GraphQL"]="https://graphql.org/"
)

animate_loading() {
    local delay=0.2
    local spin='-\|/'
    local i=0
    while :; do
        echo -n "${spin:i++%${#spin}:1}"
        sleep $delay
        echo -ne "\r"
    done
}

show_technologies() {
    clear
    echo "¡Bienvenido al roadmap de Django y tecnologías relacionadas!"
    echo
    echo "A continuación, enlace a los recursos sobre las tecnologías utilizadas en el proyecto Zetter y otras que podrían ser útiles."
    echo
    echo "Tecnologías y enlaces recomendados para aprender:"
    echo

    for tech in "${!technologies[@]}"; do
        echo " - $tech: ${technologies[$tech]}"
    done
}

message() {
    echo
    echo "¡Todo listo! Ahora puedes explorar más sobre estas tecnologías."
    echo "Recuerda seguir aprendiendo y practicando para mejorar tus habilidades."
}

animate_loading &
loading_pid=$!

sleep 3

kill $loading_pid

show_technologies

message