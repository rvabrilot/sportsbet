import { useState, useEffect } from 'react';
import { Link } from '../../components/Link';
import { eventService } from '../../services/event.service';

const Index = () => {
    const [events, setEvents] = useState(null);

    useEffect(() => {
        eventService.getAll().then(x => setEvents(x));
    }, []);

    const deleteEvent = (id) => {
        setEvents(events.map(x => {
            if (x.id === id) { x.isDeleting = true; }
            return x;
        }));
        eventService.delete(id).then(() => {
            setEvents(events => events.filter(x => x.id !== id));
        });
    }

    return (
        <div>
            <h1>Events</h1>
            <div style={{position: 'initial', float: 'right'}}>
                <Link href="/events/add" className="btn btn-outline-success md-2">+</Link>
            </div>
            
            <table className="table table-striped">
                <thead>
                    <tr>
                    <th style={{ width: '30%' }}>Category</th>
                    <th style={{ width: '30%' }}>Date</th>
                    <th style={{ width: '30%' }}>Player</th>
                        <th style={{ width: '10%' }}></th>
                    </tr>
                </thead>
                <tbody>
                    {events && events.map(event =>
                        <tr key={event.id}>
                            <td>{event.event_start}</td>
                            <td>{event.event_end}</td>
                            <td>{event.local_player} vs {event.visitor_player} </td>
                            <td style={{ whiteSpace: 'nowrap' }}>
                                <Link href={`/events/edit/${event.id}`} className="btn btn-sm btn-primary mr-1">Edit</Link>
                                <button onClick={() => deleteEvent(event.id)} className="btn btn-sm btn-danger btn-delete-user" disabled={event.isDeleting}>
                                    {event.isDeleting 
                                        ? <span className="spinner-border spinner-border-sm"></span>
                                        : <span>Delete</span>
                                    }
                                </button>
                            </td>
                        </tr>
                    )}
                    {!events &&
                        <tr>
                            <td colSpan="4" className="text-center">
                                <div className="spinner-border spinner-border-lg align-center"></div>
                            </td>
                        </tr>
                    }
                    {events && !events.length &&
                        <tr>
                            <td colSpan="4" className="text-center">
                                <div className="p-2">No events To Display</div>
                            </td>
                        </tr>
                    }
                </tbody>
            </table>
        </div>
    );
}

export default Index;
