import express from 'express';
import { availableParallelism } from 'node:os';
import cluster from 'node:cluster';

const numCPUs = availableParallelism();
console.log(numCPUs);


if (cluster.isPrimary) {
    console.log(`Primary ${process.pid} is running`);

    // Fork workers.
    for (let i = 0; i < numCPUs; i++) {
        cluster.fork();
    }

    cluster.on('exit', (worker, code, signal) => {
        console.log(`worker ${worker.process.pid} died`);
    });
} else {
    // Workers can share any TCP connection
    // In this case it is an HTTP server
    const app = express();

    app.get("/", (req, res) => {
        let sum = 0;
        for (let i = 0; i < 1000000; i++) {
            sum += i;
        }
        res.json({ message: sum });
    });

    app.listen(4400, () => console.log(`Listening on port 4400`));
    // http.createServer((req, res) => {
    //     res.writeHead(200);
    //     res.end('hello world\n');
    // }).listen(8000);

    console.log(`Worker ${process.pid} started`);
}
