from django import forms

class QuestionsForm(forms.Form):

    actors = forms.CharField(label='Who are some of your favorite actors? (seperated by a single comma, like "Tom Holland,Andrew Garfield,Tobey Macguire")', max_length=200)
    directors = forms.CharField(label='Who are some of your favorite directors? (seperated by a single comma, like "Quentin Tarantino,Steven Spielberg")', max_length=200)

    yearEarly = forms.CharField(label='What is the earliest year you would like to see a movie from?', max_length=100)
    yearLatest = forms.CharField(label='What is the latest year you would like to see a movie from?', max_length=100)
    length = forms.CharField(label='What is your optimal movie length? (in minutes, maximum 200)', max_length=100)

    #rating
    ratedr = forms.BooleanField(label='Would you like to see rated R movies?', required=False)
    ratedpg13 = forms.BooleanField(label='Would you like to see PG-13 movies?', required=False)
    ratedPG = forms.BooleanField(label='Would you like to see rated PG movies?', required=False)
    ratedG = forms.BooleanField(label='Would you like to see rated G movies?', required=False)

    #streaming services
    netflix = forms.BooleanField(label='Do you have Netflix?', required=False)
    hulu = forms.BooleanField(label='Do you have Hulu?', required=False)
    amazon = forms.BooleanField(label='Do you have Amazon Prime Video?', required=False)
    peacock = forms.BooleanField(label='Do you have Peacock?', required=False)
    hbo = forms.BooleanField(label='Do you have HBO Max?', required=False)
    disney = forms.BooleanField(label='Do you have Disney Plus?', required=False)
    paramount = forms.BooleanField(label='Do you have Paramount Plus?', required=False)
    discovery = forms.BooleanField(label='Do you have Discovery?', required=False)
    apple = forms.BooleanField(label='Do you have AppleTV?', required=False)

    #genres
    drama = forms.BooleanField(label='Do you like dramas?', required=False)
    crime = forms.BooleanField(label='Do you like crime movies?', required=False)
    action = forms.BooleanField(label='Do you like action movies?', required=False)
    thriller = forms.BooleanField(label='Do you like thriller movies?', required=False)
    history = forms.BooleanField(label='Do you like movies about history?', required=False)
    war = forms.BooleanField(label='Do you like movies about war?', required=False)
    adventure = forms.BooleanField(label='Do you like adventure movies?', required=False)
    fantasy = forms.BooleanField(label='Do you like fantasy movies?', required=False)
    western = forms.BooleanField(label='Do you like Western movies?', required=False)
    comedy = forms.BooleanField(label='Do you like comedies?', required=False)
    romance = forms.BooleanField(label='Do you like romance movies?', required=False)
    scifi = forms.BooleanField(label='Do you like Science Fiction movies?', required=False)
    mystery = forms.BooleanField(label='Do you like mystery movies?', required=False)
    family = forms.BooleanField(label='Do you like family movies?', required=False)
    animation = forms.BooleanField(label='Do you like animated movies?', required=False)
    horror = forms.BooleanField(label='Do you like horror movies?', required=False)
    music = forms.BooleanField(label='Do you like musicals?', required=False)
