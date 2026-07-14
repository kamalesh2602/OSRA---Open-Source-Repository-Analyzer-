import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    Tooltip,
    Legend,
} from "chart.js";

import { Bar } from "react-chartjs-2";

ChartJS.register(
    CategoryScale,
    LinearScale,
    BarElement,
    Tooltip,
    Legend
);

interface Props {
    repository: any;
}

export default function RepositoryChart({ repository }: Props) {
    const data = {
        labels: [
            "Stars",
            "Forks",
            "Watchers",
            "Issues",
        ],

        datasets: [
            {
                label: "Repository Metrics",

                data: [
                    repository.stars,
                    repository.forks,
                    repository.watchers,
                    repository.open_issues,
                ],
            },
        ],
    };

    return (
        <div className="rounded-3xl border border-white/10 bg-white/5 p-6">
            <h2 className="mb-6 text-xl font-semibold">
                Repository Metrics
            </h2>

            <Bar data={data} />
        </div>
    );
}