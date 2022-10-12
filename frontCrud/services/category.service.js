import { apiUrl } from 'config';
import { fetchWrapper } from 'helpers';

export const categoryService = {
    getAll,
    getById,
    create,
    update,
    delete: _delete
};

const baseUrl = `${apiUrl}`;//event_category

function getAll() {
    return fetchWrapper.get(`${apiUrl}/event_category`);
}

function getById(id) {
    return fetchWrapper.get(`${baseUrl}/event_category/${id}`);
}

function create(params) {
    return fetchWrapper.post(`${baseUrl}/event_category`, params);
}

function update(id, params) {
    return fetchWrapper.put(`${baseUrl}/update_event_category`, params);
}

function _delete(id) {
    return fetchWrapper.delete(`${baseUrl}/${id}`);
}
