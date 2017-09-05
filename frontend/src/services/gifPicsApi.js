import axios from 'axios';

export default {
    getRandomPics() {
        return axios.get('/api/pics/').then(response =>
        {
            return response.data.pics;
        });
    },
    search(q) {
        const params = {
            q,
        };
        return axios.get('/api/search/', {params: params}).then(response => {
            return response.data.pics;
        });
    },
    getSuggestions(q) {
        const params = {
            q,
        };
        return axios.get('/api/search_suggestions/', {params: params}).then(response => {
            return response.data.suggestions;
        });
    },
    getDetail(id) {
        return axios.get('/api/pics/' + id).then(response => {
            return response.data;
        });
    },
}