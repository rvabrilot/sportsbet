import { apiUrl } from 'config';
import { fetchWrapper } from 'helpers';

export const userService = {
    getAll,
    getById,
    create,
    update,
    delete: _delete
};

const baseUrl = `${apiUrl}`;

function getAll() {
    return fetchWrapper.get(`${baseUrl}/user`);
}

function getById(id) {
    return fetchWrapper.get(`${baseUrl}/user/${id}`);
}

function create(params) {
    return fetchWrapper.post(`${baseUrl}/user`, params);
}

function update(id, params) {
    return fetchWrapper.put(`${baseUrl}/update_user`, params);
}

function _delete(id) {
    return fetchWrapper.delete(`${baseUrl}/user/${id}`);
}
