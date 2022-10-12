import { useState, useEffect } from 'react';
import { Link } from '../../components/Link';
import { betService } from '../../services/bet.service';

const Index = () => {
    const [bets, setBets] = useState(null);

    useEffect(() => {
        betService.getAll().then(x => setBets(x));
    }, []);

    const deleteBet = (id) => {
        betService(bets.map(x => {
            if (x.id === id) { x.isDeleting = true; }
            return x;
        }));
        betService.delete(id).then(() => {
            setBets(bets => bets.filter(x => x.id !== id));
        });
    }

    return (
        <div>
            <h1>Bets</h1>
            <div style={{position: 'initial', float: 'right'}}>
                <Link href="/bets/add" className="btn btn-outline-success md-2">+</Link>
            </div>
            
            <table className="table table-striped">
                <thead>
                    <tr>
                    <th style={{ width: '30%' }}>Event</th>
                    <th style={{ width: '30%' }}>Status</th>
                        <th style={{ width: '10%' }}></th>
                    </tr>
                </thead>
                <tbody>
                    {bets && bets.map(bet =>
                        <tr key={bet.id}>
                            <td>{bet.event_id}</td>
                            <td>{bet.status}</td>
                            <td style={{ whiteSpace: 'nowrap' }}>
                                <Link href={`/bets/edit/${bet.id}`} className="btn btn-sm btn-primary mr-1">Edit</Link>
                                <button onClick={() => deleteBet(bet.id)} className="btn btn-sm btn-danger btn-delete-user" disabled={bet.isDeleting}>
                                    {bet.isDeleting 
                                        ? <span className="spinner-border spinner-border-sm"></span>
                                        : <span>Delete</span>
                                    }
                                </button>
                            </td>
                        </tr>
                    )}
                    {!bets &&
                        <tr>
                            <td colSpan="4" className="text-center">
                                <div className="spinner-border spinner-border-lg align-center"></div>
                            </td>
                        </tr>
                    }
                    {bets && !bets.length &&
                        <tr>
                            <td colSpan="4" className="text-center">
                                <div className="p-2">No category To Display</div>
                            </td>
                        </tr>
                    }
                </tbody>
            </table>
        </div>
    );
}

export default Index;
