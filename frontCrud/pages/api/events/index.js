import { eventsRepo } from 'helpers';

export default handler;

function handler(req, res) {
    switch (req.method) {
        case 'GET':
            return getEvents();
        case 'POST':
            return createEvent();
        default:
            return res.status(405).end(`Method ${req.method} Not Allowed`)
    }

    function getEvents() {
        const events = eventsRepo.getAll();
        return res.status(200).json(categorys);
    }
    
    function createEvent() {
        try {
            eventsRepo.create(req.body);
            return res.status(200).json({});
        } catch (error) {
            return res.status(400).json({ message: error });
        }
    }
}
