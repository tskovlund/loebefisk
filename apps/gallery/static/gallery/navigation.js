function leftArrowPressed() {
    window.location = "{% url 'gallery:post' p.pk %}";
}

function rightArrowPressed() {
    window.location = "{% url 'gallery:post' p.pk %}";
}

document.onkeydown = function(evt) {
    evt = evt || window.event;
    switch (evt.keyCode) {
        case 37:
            {% with post.get_previous as p %} 
            {% if p %}
            leftArrowPressed();
            break;
            {% endif %}
            {% endwith %}
        case 39:
            {% with post.get_next as p %} 
            {% if p %}
            rightArrowPressed();
            break;
            {% endif %}
            {% endwith %}
    }
};
