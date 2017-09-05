import axios from 'axios';

export default {
    getRandomPics() {
        return axios.get('/api/pics').then(response =>
        {
            return response.data.pics;
        });
    },
}