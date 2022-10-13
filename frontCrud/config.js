const apiUrl = process.env.NODE_ENV === 'development' 
    ? 'http://localhost:8080/api/v3' // development api 
    : 'http://localhost:3000/api'; // production api

export {
    apiUrl
};