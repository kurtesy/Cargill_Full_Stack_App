import axios from 'axios';

const headers = {
    'Content-Type': 'application/json',
    "Access-Control-Allow-Origin": "*",
  }
  

const getData = async (teamName) => {
    const data = await axios.get(`http://127.0.0.1:5000/get_team/${teamName}`,
                                {headers: headers})
        .then(res => {
            const roles = res.data;
            return roles
        })
        .catch(err => {
            console.log('GET request failed with error', err)
            return [err.message];
        })
    return data;
};

const postData = async (data) => {
    const status = await axios.post(`http://127.0.0.1:5000/add_team`, JSON.stringify(data), {headers: headers})
        .then(res => {
            const status = res.data;
            return status
        })
        .catch(err => {
            console.log('POST request failed with error', err)
            return err;
        })
    return status;
};


export {getData, postData};
