import { apiUrl } from 'config';
import { fetchWrapper } from 'helpers';

export const playerService = {
    getAll,
    getById,
    create,
    update,
    delete: _delete
};

const baseUrl = `${apiUrl}`;// players

function getAll() {
    return fetchWrapper.get(`${apiUrl}/event_player`);
}

function getById(id) {
    return fetchWrapper.get(`${baseUrl}/event_player/${id}`);
}

function create(params) {
    return fetchWrapper.post(`${baseUrl}/event_player`, params);
}

function update(id, params) {
    return fetchWrapper.put(`${baseUrl}/update_event_player`, params);
}

function _delete(id) {
    return fetchWrapper.delete(`${baseUrl}/${id}`);
}
