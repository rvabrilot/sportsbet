import { Link } from 'components';

const Home = () => {
    return (
        <div>
            <p><Link href="/users">&gt;&gt; Manage Users</Link></p>
            <p><Link href="/bets">&gt;&gt; bets</Link></p>
            <p><Link href="/events">&gt;&gt; events</Link></p>
            <p><Link href="/eventCategorys">&gt;&gt; event Categorys</Link></p>
            <p><Link href="/eventPlayers">&gt;&gt; event Players</Link></p>
        </div>
    );
}

export default Home;