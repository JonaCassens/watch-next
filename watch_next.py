import spacy

nlp = spacy.load('en_core_web_md')

description = 'Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where Hulk can live in peace. Unfortunately, Hulk lands on planet Sakaar where he is sold into slavery and trained as a gladiator.'

def similarMovie(description):
    movie_choice = ''
    similarity_score = 0
    model_desc = nlp(description)
    with open('movies.txt', 'r') as f:
        for line in f:
            similarity = nlp(line).similarity(model_desc)
            if similarity > similarity_score:
                similarity_score = similarity
                movie_choice = line.split(':')[0]
    return f'Recommended movie: {movie_choice}'

print(similarMovie(description))
