import { NavLink } from '.';

export const Nav = () => {
    return (
        <nav className="navbar navbar-expand navbar-dark bg-dark">
            <div className="navbar-nav">
                <NavLink href="/" exact className="nav-item nav-link">Home</NavLink>
                <NavLink href="/users" className="nav-item nav-link">Users</NavLink>
                <NavLink href="/users" className="nav-item nav-link">Sports</NavLink>
                <NavLink href="/users" className="nav-item nav-link">Bets</NavLink>
            </div>
        </nav>
    );
}