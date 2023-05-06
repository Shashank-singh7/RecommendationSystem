import streamlit as st

import pickle
import requests

def poster(movie_id):
    responce=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=f6d636bb91beca91dc7dc985e775130f&language=en-US".format(movie_id))
    details=responce.json()
    return "https://image.tmdb.org/t/p/w500/" + details['poster_path']

def recommend(movie):
    index=data[data["title"]==movie].index[0]
    distance=similar_score[index]
    movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:7]
    l=[]
    p=[]
    d=[]
    r=[]
    for i in movie_list:
        movieid=data.iloc[i[0]].movie_id
        l.append(data.iloc[i[0]].title)
        p.append(poster(movieid))
        d.append((desc(movieid)))
        r.append(rating(movieid))
    return l,p,d,r

def desc(movie_id):
    responce=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=f6d636bb91beca91dc7dc985e775130f&language=en-US".format(movie_id))
    details=responce.json()
    return details["overview"]
def rating(movie_id):
    responce = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=f6d636bb91beca91dc7dc985e775130f&language=en-US".format(movie_id))
    details = responce.json()
    return  details["vote_average"]





st.set_page_config(layout="wide")

#data = pickle.load(open("data.pkl","rb"))
data=pd.read_pickle('data.pkl')
similar_score=pickle.load(open("similar_score.pkl","rb"))


st.title("MOVIES RECOMMENDER")
col1,col2=st.columns((7,1))
with col1:
    option=st.selectbox("Enter movie name",data["title"].to_list())
    butn = st.button("Recommend")
with col2:
    st.image(poster(data.loc[data[data["title"] == option].index[0]].at["movie_id"]))
if butn:
    #st.markdown("<h1 style='text-align: center; color: red;'>Related movies</h1>", unsafe_allow_html=True)
    st.header("Related movies")
    recommended_list,poster_path_list,desc_list,rating_list= recommend(option)
    c1,c2,c3,c4,c5,c6=st.columns(6)
    with c1:
        st.image(poster_path_list[0])
        st.subheader(recommended_list[0].upper())
        st.text("Ratings-{}".format(rating_list[0]))
        st.text(desc_list[0])
    with c2:
        st.image(poster_path_list[1])
        st.subheader(recommended_list[1].upper())
        st.text("Rating-{}".format(rating_list[1]))
        st.text(desc_list[1])
    with c3:
        st.image(poster_path_list[2])
        st.subheader(recommended_list[2].upper())
        st.text("Rating-{}".format(rating_list[2]))
        st.text(desc_list[2])
    with c4:
        st.image(poster_path_list[3])
        st.subheader(recommended_list[3].upper())
        st.text("Rating-{}".format(rating_list[3]))
        st.text(desc_list[3])
    with c5:
        st.image(poster_path_list[4])
        st.subheader(recommended_list[4].upper())
        st.text("Rating-{}".format(rating_list[4]))
        st.text(desc_list[4])
    with c6:
        st.image(poster_path_list[5])
        st.subheader(recommended_list[5].upper())
        st.text("Rating-{}".format(rating_list[5]))
        st.text(desc_list[5])


