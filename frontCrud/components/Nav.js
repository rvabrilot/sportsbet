import { NavLink } from '.';

export const Nav = () => {
    return (
        <nav className="navbar navbar-expand">
            <div className="navbar-nav">
                <NavLink href="/" exact className="nav-item nav-link">Home</NavLink>
                <NavLink href="/users" className="btn btn-light">users</NavLink>
                <NavLink href="/bets" className="btn btn-light">bets</NavLink>
                <NavLink href="/events" className="btn btn-light">events</NavLink>
                <NavLink href="/eventPlayers" className="btn btn-light">event_player</NavLink>
                <NavLink href="/eventCategorys" className="btn btn-light">event_categorys</NavLink>
            </div>
        </nav>
    );
}