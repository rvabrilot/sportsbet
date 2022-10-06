import { NavLink } from '.';

export const Nav = () => {
    return (
        <nav className="navbar navbar-expand">
            <div className="navbar-nav">
                <NavLink href="/" exact className="nav-item nav-link">Home</NavLink>
                <NavLink href="/users" className="btn btn-light">users</NavLink>
                <NavLink href="/eventCategorys" className="btn btn-light">event_category</NavLink>
                <NavLink href="/eventPlayer" className="btn btn-light">event_player</NavLink>
            </div>
        </nav>
    );
}