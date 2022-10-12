import { eventsRepo } from 'helpers';

export default handler;

function handler(req, res) {
    switch (req.method) {
        case 'GET':
            return getEventRepoById();
        case 'PUT':
            return updateEvent();
        case 'DELETE':
            return deleteEvent();
        default:
            return res.status(405).end(`Method ${req.method} Not Allowed`)
    }

    function getEventRepoById() {
        const event = eventsRepo.getById(req.query.id);
        return res.status(200).json(event);
    }

    function updateEvent() {
        try {
            eventsRepo.update(req.query.id, req.body);
            return res.status(200).json({});
        } catch (error) {
            return res.status(400).json({ message: error });
        }
    }

    function deleteEvent() {
        eventsRepo.delete(req.query.id);
        return res.status(200).json({});
    }
}
