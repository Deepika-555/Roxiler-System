import React, { useEffect, useState } from 'react';
import axios from 'axios';
import TransactionsTable from './components/TransactionsTable';
import Statistics from './components/Statistics';
import BarChart from './components/BarChart';

const App = () => {
    const [month, setMonth] = useState(3); // Default to March
    const [search, setSearch] = useState('');
    const [transactions, setTransactions] = useState([]);
    const [statistics, setStatistics] = useState({});
    const [barChartData, setBarChartData] = useState([]);
    const [page, setPage] = useState(1);

    const fetchTransactions = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:8000/api/transactions`, {
                params: {
                    month,
                    search,
                    page,
                    limit: 10
                }
            });
            setTransactions(response.data);
        } catch (error) {
            console.error('Error fetching transactions:', error);
        }
    };

    const fetchStatistics = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:8000/api/statistics`, {
                params: { month }
            });
            setStatistics(response.data);
        } catch (error) {
            console.error('Error fetching statistics:', error);
        }
    };

    const fetchBarChartData = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:8000/api/barchart`, {
                params: { month }
            });
            setBarChartData(response.data);
        } catch (error) {
            console.error('Error fetching bar chart data:', error);
        }
    };

    useEffect(() => {
        fetchTransactions();
        fetchStatistics();
        fetchBarChartData();
    }, [month, search, page]);

    return (
        <div>
            <h1>Transactions Dashboard</h1>
            <div>
                <label>Month:</label>
                <select value={month} onChange={(e) => setMonth(parseInt(e.target.value))}>
                    <option value={1}>January</option>
                    <option value={2}>February</option>
                    <option value={3}>March</option>
                    <option value={4}>April</option>
                    <option value={5}>May</option>
                    <option value={6}>June</option>
                    <option value={7}>July</option>
                    <option value={8}>August</option>
                    <option value={9}>September</option>
                    <option value={10}>October</option>
                    <option value={11}>November</option>
                    <option value={12}>December</option>
                </select>
            </div>
            <div>
                <label>Search:</label>
                <input type="text" value={search} onChange={(e) => setSearch(e.target.value)} />
            </div>
            <Statistics statistics={statistics} />
            <TransactionsTable transactions={transactions} page={page} setPage={setPage} />
            <BarChart data={barChartData} />
        </div>
    );
};

export default App;
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import TransactionsTable from './components/TransactionsTable';
import Statistics from './components/Statistics';
import BarChart from './components/BarChart';

const App = () => {
    const [month, setMonth] = useState(3); // Default to March
    const [search, setSearch] = useState('');
    const [transactions, setTransactions] = useState([]);
    const [statistics, setStatistics] = useState({});
    const [barChartData, setBarChartData] = useState([]);
    const [page, setPage] = useState(1);

    const fetchTransactions = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:8000/api/transactions`, {
                params: {
                    month,
                    search,
                    page,
                    limit: 10
                }
            });
            setTransactions(response.data);
        } catch (error) {
            console.error('Error fetching transactions:', error);
        }
    };

    const fetchStatistics = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:8000/api/statistics`, {
                params: { month }
            });
            setStatistics(response.data);
        } catch (error) {
            console.error('Error fetching statistics:', error);
        }
    };

    const fetchBarChartData = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:8000/api/barchart`, {
                params: { month }
            });
            setBarChartData(response.data);
        } catch (error) {
            console.error('Error fetching bar chart data:', error);
        }
    };

    useEffect(() => {
        fetchTransactions();
        fetchStatistics();
        fetchBarChartData();
    }, [month, search, page]);

    return (
        <div>
            <h1>Transactions Dashboard</h1>
            <div>
                <label>Month:</label>
                <select value={month} onChange={(e) => setMonth(parseInt(e.target.value))}>
                    <option value={1}>January</option>
                    <option value={2}>February</option>
                    <option value={3}>March</option>
                    <option value={4}>April</option>
                    <option value={5}>May</option>
                    <option value={6}>June</option>
                    <option value={7}>July</option>
                    <option value={8}>August</option>
                    <option value={9}>September</option>
                    <option value={10}>October</option>
                    <option value={11}>November</option>
                    <option value={12}>December</option>
                </select>
            </div>
            <div>
                <label>Search:</label>
                <input type="text" value={search} onChange={(e) => setSearch(e.target.value)} />
            </div>
            <Statistics statistics={statistics} />
            <TransactionsTable transactions={transactions} page={page} setPage={setPage} />
            <BarChart data={barChartData} />
        </div>
    );
};

export default App;
