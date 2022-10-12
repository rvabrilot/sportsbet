import Head from 'next/head';
import 'styles/globals.css';
import { Nav } from '../components/Nav';
import { Alert } from '../components/Alert';

const App = ({ Component, pageProps }) => {
    return (
        <>
            <Head>
                <title></title>
                <link href="//netdna.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet" />
            </Head>

            <div className="app-container bg-light">
                <Nav />
                <Alert />
                <div className="container pt-4 pb-4">
                    <Component {...pageProps} />
                </div>
            </div>

        </>
    );
}

export default App;