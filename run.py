{% extends "base.html" %}
{% block content %}

    <h2>{{ page_title }}</h2>
    <p>
        The formation of the group grew out of a meeting Gandalf had with Thorin in Bree which kindled Thorins interest in
		recapturing his long lost family inheritance. (Thorin's grandfather had been the king of the Lonely Mountain when
		Smaug came and took it.) Remembering that he had once known an adventurous Hobbit on his travels in the Shire,
		Gandalf decided to add Bilbo to their company because he knew that stealth and cunning were preferable to force.
		Gandalf also believed that someone like Bilbo could keep the sometimes prideful and stubborn Dwarves from rash
		action. The superstitious Dwarves also considered thirteen to be an unlucky number, and as Gandalf had planned to
		leave on other business, welcomed a fourteenth to fill into their party.
    </p>

    {% for member in company %}

        <div class="row featurette">

            {% if loop.index % 2 != 0 %}

                <div class="col-md-7">
                    <h3><a href="/about/{{ member.url }}">{{ loop.index }}. {{ member.name }}</a></h3>
                    <p>{{ member.description }}</p>
                </div>
                <div class="col-md-5">
                    <img src="{{ member.image_source }}" alt="" class="featurette-image image-responsive">
                </div>
            
            {% else %}

                <div class="col-md-5">
                    <img src="{{ member.image_source }}" alt="" class="featurette-image image-responsive">
                </div>
                <div class="col-md-7">
                    <h3><a href="/about/{{ member.url }}">{{ loop.index }}. {{ member.name }}</a></h3>
                    <p>{{ member.description }}</p>
                </div>

            {% endif %}

        </div>

        {% if loop.index != loop.length %}

            <hr class="featurette-divider">

        {% endif %}

    {% endfor %}

{% endblock %}