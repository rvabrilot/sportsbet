import { Link } from 'components';

const Home = () => {
    return (
        <div>
            <p><Link href="/users">&gt;&gt; Manage Users</Link></p>
            <p><Link href="/eventCategorys">&gt;&gt; event Categorys</Link></p>
        </div>
    );
}

export default Home;