#include <iostream>
#include <fstream>
#include <cstdlib>
#include <iomanip>
#include <locale>
#include <sstream>
#include <vector>
#include <algorithm>
#include <set>
#include <random>
#include <chrono>
#include <unordered_map>
#include <unordered_set>
#include <map>

using namespace std;


const int MIN_SIZE = 2;
const int MAX_SIZE = 4;

const int PRIME = 7; // Prime number for hashing


vector<vector<int>> all_simplices, simplices; // Vector to store all simplices

vector<set<int>> all_nei, nei; // Adjacency list (edges)
set<int> tri;   // Set of triangle hashes
set<int> quad;  // Set of tetrahedron hashes

 int maxVertex = 0; // To find the largest vertex index

 string formatNumber(int num) {
     stringstream ss;
     // Set the locale to the default "en_US" to use comma as a thousands separator
     ss.imbue(locale("en_US.UTF-8"));
     ss << fixed << num;
     return ss.str();
 }

// Simplet Hash Index
map<int, int> simpletIndexMap = {
    {2005, 1}, {3015, 2}, {3020, 3}, {3031, 4}, {4029, 5},
    {4039, 6}, {4050, 7}, {4046, 8}, {4057, 9}, {4068, 10},
    {4031, 11}, {4034, 12}, {4051, 13}, {4062, 14}, {4073, 15},
    {4084, 16}, {4095, 17}, {4108, 18}
};

int findSimpletIndex(int number) {
     auto it = simpletIndexMap.find(number);

     if (it != simpletIndexMap.end()) {
         return it->second;
     } else {
         return -1;  // not found
     }
 }


 // Function to select a connected component of k vertices using BFS.
 // If a connected component with at least k vertices is found,
 // the function returns the first k vertices in that component;
 // otherwise, it returns an empty vector.
 vector<int> selectConnectedVertices(const vector<set<int>>& nei, int k) {
     int n = nei.size();
     // Try each vertex as a starting point for BFS
     for (int start = 0; start < n; ++start) {
         vector<bool> visited(n, false);
         vector<int> component;
         queue<int> q;

         // Start BFS from vertex 'start'
         q.push(start);
         visited[start] = true;

         while (!q.empty() && component.size() < (size_t)k) {
             int cur = q.front();
             q.pop();
             component.push_back(cur);

             // Enqueue unvisited neighbors
             for (int neighbor : nei[cur]) {
                 if (neighbor >= 0 && neighbor < n && !visited[neighbor]) {
                     visited[neighbor] = true;
                     q.push(neighbor);
                 }
             }
         }

         // If we found at least k connected vertices, return the first k vertices
         if (component.size() >= (size_t)k) {
             return vector<int>(component.begin(), component.begin() + k);
         }
     }

     // If no connected component of size k is found, return an empty vector
     return {};
 }

 // Function to filter simplices that contain only vertices from connectedVertices.
// Input:
//    simplices - a vector of simplices (each simplex is a vector of vertex indices)
//    connectedVertices - a vector of vertex indices that are considered as selected/connected
// Output:
//    A vector of simplices (vector<vector<int>>) such that each simplex contains only vertices present in connectedVertices.
void filterSimplices(const vector<vector<int>>& all_simplices, const vector<int>& connectedVertices) {
    // Create a set for fast lookup of connected vertices
    set<int> selectedVertices(connectedVertices.begin(), connectedVertices.end());

    // Loop over each simplex
    for (const auto& simplex : all_simplices) {
        bool valid = true;
        // Check if every vertex in the simplex is in the selectedVertices set
        for (int vertex : simplex) {
            if (selectedVertices.find(vertex) == selectedVertices.end()) {
                valid = false;
                break;
            }
        }
        // If valid, add this simplex to the result
        if (valid) {
            simplices.push_back(simplex);
        }
    }
}


int bfsFurthest(const vector<set<int>>& nei, int start) {
    int n = nei.size();
    vector<int> dist(n, -1);
    queue<int> q;
    dist[start] = 0;
    q.push(start);

    int furthest = start;

    while (!q.empty()) {
        int v = q.front();
        q.pop();
        for (int neighbor : nei[v]) {
            if (dist[neighbor] == -1) {
                dist[neighbor] = dist[v] + 1;
                q.push(neighbor);
                if (dist[neighbor] > dist[furthest]) {
                    furthest = neighbor;
                }
            }
        }
    }

    return dist[furthest]; // distance to furthest node
}

void fastGraphProperties(const vector<set<int>>& nei) {
    int n = nei.size();
    int maxDegree = 0;
    int size = 0;

    // Find graph size
    for (int i = 0; i < n; ++i)
        if (!nei[i].empty())
          size++;

    // Find a starting node with non-zero degree
    int start = -1;
    for (int i = 0; i < n; ++i) {
        if (!nei[i].empty()) {
            start = i;
            break;
        }
    }

    if (start == -1) {
        cout << "Graph is empty.\n";
        return;
    }

    // 1st BFS to find a far node
    int firstBFS = -1, maxDist = 0;
    {
        vector<int> dist(n, -1);
        queue<int> q;
        dist[start] = 0;
        q.push(start);
        while (!q.empty()) {
            int v = q.front(); q.pop();
            for (int u : nei[v]) {
                if (dist[u] == -1) {
                    dist[u] = dist[v] + 1;
                    q.push(u);
                    if (dist[u] > maxDist) {
                        maxDist = dist[u];
                        firstBFS = u;
                    }
                }
            }
        }
    }

    // 2nd BFS from the farthest node
    int diameter = bfsFurthest(nei, firstBFS);

    // Max degree
    for (const auto& s : nei) {
        if ((int)s.size() > maxDegree)
            maxDegree = s.size();
    }

    cout << endl;
    cout << "Graph Size: " << formatNumber(size) << endl;
    cout << "Number of Simplices: " << formatNumber(simplices.size()) << endl;
    cout << "Approximate Graph Diameter: " << formatNumber(diameter) << endl;
    cout << "Maximum Vertex Degree: " << formatNumber(maxDegree) << endl;
}

// Function to compute a hash for a sorted set of vertices
int computeHash(const vector<int>& vertices) {
    int hashValue = 0;
    int power = 1;
    for (int v : vertices) {
        hashValue += v * power;
        power *= PRIME;
    }
    return hashValue;
}

// Updated function to hash the simplex considering both degree counts and 3-simplices (triangles)
int hashSimplex(const set<int>& simplex) {
    vector<int> nodes(simplex.begin(), simplex.end());
    int n = nodes.size();
    vector<int> degrees(n, 0);

    // Count degrees within the simplex
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            // If there's an edge between two vertices, increment their degrees
            if (simplex.count(nodes[i]) && simplex.count(nodes[j])) {
                degrees[i]++;
                degrees[j]++;
            }
        }
    }

    // Sort degrees to make the order irrelevant
    sort(degrees.begin(), degrees.end());

    // Multiply each degree by a prime number2
    const vector<int> primes = {2, 3, 5, 7}; // For up to 4 nodes
    int hash = 0;
    for (int i = 0; i < n; ++i) {
        hash += degrees[i] * primes[i];
    }

    // Count 3-simplices (triangles) and multiply by a prime number
    int triangle_count = 0;
    if (n >= 3) {
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                for (int k = j + 1; k < n; ++k) {
                    vector<int> triangle = {nodes[i], nodes[j], nodes[k]};
                    sort(triangle.begin(), triangle.end());
                    int tri_hash = computeHash(triangle);
                    if (tri.count(tri_hash)) {
                        triangle_count++; // Count the triangle
                    }
                }
            }
        }
    }

    // Count 4-simplices (tetrahedra) and multiply by a different prime number
    int tetrahedron_count = 0;
    if (n == 4) {
        vector<int> tetrahedron = {nodes[0], nodes[1], nodes[2], nodes[3]};
        sort(tetrahedron.begin(), tetrahedron.end());
        int quad_hash = computeHash(tetrahedron);
        if (quad.count(quad_hash)) {
            tetrahedron_count++; // Count the tetrahedron
        }
    }

    // Multiply the triangle count by a prime number (e.g., 11) and tetrahedron count by another prime number (e.g., 13)
    hash += triangle_count * 11;  // Multiply by prime for triangles
    hash += tetrahedron_count * 13;  // Multiply by prime for tetrahedra

    // Add the size of the simplex as an offset to separate different simplex sizes
    hash += 1000 * n;

    return hash;
}

// Function to get a random index in a range
int getRandomIndex(int maxIndex) {
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> dist(0, maxIndex - 1);
    return dist(gen);
}

// Function to get a random simplex from a list
vector<int> getRandomNeighbor(const vector<vector<int>>& neighbors) {
    if (neighbors.empty()) return {}; // No valid moves
    return neighbors[getRandomIndex(neighbors.size())];
}

// Function to check if a simplex is connected
bool isConnected(const vector<int>& simplex) {
    if (simplex.empty()) return false;

    set<int> visited;
    queue<int> q;
    q.push(simplex[0]); // Start BFS from the first vertex
    visited.insert(simplex[0]);

    while (!q.empty()) {
        int v = q.front();
        q.pop();

        for (int neighbor : nei[v]) {
            if (visited.count(neighbor) == 0 && find(simplex.begin(), simplex.end(), neighbor) != simplex.end()) {
                visited.insert(neighbor);
                q.push(neighbor);
            }
        }
    }

    return visited.size() == simplex.size();
}

bool isConnectedFast(const vector<int>& simplex) {
    int sz = simplex.size();
    if (sz < 2) return false;
    if (sz == 2) {
        // Two vertices: check if there's an edge
        return nei[simplex[0]].count(simplex[1]);
    }

    // Build subgraph adjacency between vertices in simplex
    int count = 0;
    for (int i = 0; i < sz; ++i) {
        for (int j = i + 1; j < sz; ++j) {
            if (nei[simplex[i]].count(simplex[j]))
                count++;
        }
    }

    // For k nodes, minimum k - 1 edges needed to be connected
    return count >= sz - 1;
}


void load_simplices(string inputFile1, string inputFile2) {
    ifstream simplex_size_file(inputFile1); // Open the file for reading
    ifstream simplex_file(inputFile2); // Open the file for reading

    if (!simplex_size_file or !simplex_file) {
        cerr << "Error: File not found!" << endl;
        return;
    }

    int size;
    while (simplex_size_file >> size) { // Read until the end of the file
      vector<int> simplex;
      int vertex;

      for (int i = 0; i < size; i++) {
          if (!(simplex_file >> vertex)) {
              cerr << "Error: Not enough data in simplex.txt!" << endl;
              return;
          }
          maxVertex = max(maxVertex, vertex);

          if (size <= 4)
              simplex.push_back(vertex);
      }

      if (size <= 4) {
          sort(simplex.begin(), simplex.end());
          all_simplices.push_back(simplex); // Store the simplex in the vector
      }
  }

  cout << "Number of Vertices: " << formatNumber(all_simplices.size()) << endl;

  simplex_file.close();
  simplex_size_file.close(); // Close the file
}

void construct_all_neighbors() {
    // Resize adjacency list, triangle set, and tetrahedron set
    all_nei.resize(maxVertex + 1);

    for (const auto& simplex : all_simplices) {
        int size = simplex.size();

        // Process edges (pairs)
        for (int i = 0; i < size; i++) {
            for (int j = i + 1; j < size; j++) {
                all_nei[simplex[i]].insert(simplex[j]);
                all_nei[simplex[j]].insert(simplex[i]);
            }
        }
    }
}

void construct_complex() {
    // Resize adjacency list, triangle set, and tetrahedron set
    nei.resize(maxVertex + 1);

    for (const auto& simplex : simplices) {
        int size = simplex.size();

        // Process edges (pairs)
        for (int i = 0; i < size; i++) {
            for (int j = i + 1; j < size; j++) {
                nei[simplex[i]].insert(simplex[j]);
                nei[simplex[j]].insert(simplex[i]);
            }
        }

        // Process triangles (triples)
        if (size >= 3) {
            for (int i = 0; i < size; i++) {
                for (int j = i + 1; j < size; j++) {
                    for (int k = j + 1; k < size; k++) {
                        vector<int> triVertices = {simplex[i], simplex[j], simplex[k]};
                        sort(triVertices.begin(), triVertices.end());
                        int triHash = computeHash(triVertices);
                        tri.insert(triHash);
                    }
                }
            }
        }

        // Process tetrahedrons (quadruples)
        if (size >= 4) {
            for (int i = 0; i < size; i++) {
                for (int j = i + 1; j < size; j++) {
                    for (int k = j + 1; k < size; k++) {
                        for (int l = k + 1; l < size; l++) {
                            vector<int> quadVertices = {simplex[i], simplex[j], simplex[k], simplex[l]};
                            sort(quadVertices.begin(), quadVertices.end());
                            int quadHash = computeHash(quadVertices);
                            quad.insert(quadHash);
                        }
                    }
                }
            }
        }
      }
}

/** Random Walk **/
// Generate all neighboring simplices while ensuring connectivity
vector<vector<int>> getNeighbors(const set<int>& currentSimplex) {
    vector<vector<int>> neighbors;

    // Convert set to sorted vector
    vector<int> simplexVec(currentSimplex.begin(), currentSimplex.end());

    // 1️⃣ **Remove one vertex (if size > 2)**
    if (currentSimplex.size() > MIN_SIZE) {
        for (int v : simplexVec) {
            vector<int> newSimplex = simplexVec;
            newSimplex.erase(remove(newSimplex.begin(), newSimplex.end(), v), newSimplex.end());
            if (isConnectedFast(newSimplex)) {
                neighbors.push_back(newSimplex);
            }
        }
    }

    set<int> candidateVertices;

    // 2️⃣ **Add one vertex (if size < 4)**
    if (currentSimplex.size() < MAX_SIZE) {
        // create candidate vertices
        for (int v : simplexVec) {
            for (int neighbor : nei[v]) {
                if (currentSimplex.count(neighbor) == 0) { // Ensure uniqueness
                    candidateVertices.insert(neighbor);
                }
            }
        }

        for (int newV : candidateVertices) {
            vector<int> newSimplex = simplexVec;
            newSimplex.push_back(newV);
            sort(newSimplex.begin(), newSimplex.end());
            if (isConnectedFast(newSimplex)) {
                neighbors.push_back(newSimplex);
            }
        }
    }

    // 3️⃣ **Swap one vertex (remove one, add another)**
    if (currentSimplex.size() > MIN_SIZE && currentSimplex.size() < MAX_SIZE) {
        for (int v : simplexVec) {
            for (int newV : candidateVertices) {
                vector<int> newSimplex = simplexVec;
                replace(newSimplex.begin(), newSimplex.end(), v, newV);
                sort(newSimplex.begin(), newSimplex.end());
                if (isConnectedFast(newSimplex)) {
                    neighbors.push_back(newSimplex);
                }
            }
        }
    }

    return neighbors;
}

set<int> randomWalk(vector<vector<int>>& simplices, int steps) {
    set<int> currentSimplex;

    if (simplices.empty()) {
        cerr << "Error: No simplices available!" << endl;
        return currentSimplex;
    }

    // Pick a random starting simplex
    int currentIndex;
    do {
        currentIndex = getRandomIndex(simplices.size());
    } while (simplices[currentIndex].size() <= 1);
    currentSimplex = set<int>(simplices[currentIndex].begin(), simplices[currentIndex].end());

    // cout << "Starting simplex: { ";
    // for (int v : currentSimplex) cout << v << " ";
    // cout << "}\n";

    // Create a random engine and a distribution
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(0.0, 1.0);

    vector<vector<int>> neighbors = getNeighbors(currentSimplex);
    for (int step = 0; step < steps; step++) {

        if (neighbors.empty()) {
            cout << "No valid moves available, stopping walk.\n";
            break;
        }

        int random = getRandomIndex(neighbors.size());
        set<int> nextSimplex = set<int>(neighbors[random].begin(), neighbors[random].end());
        vector<vector<int>> nextNeighbors = getNeighbors(currentSimplex);


        double acceptance_probability = std::min(static_cast<double>(neighbors.size()) /
                                           static_cast<double>(nextNeighbors.size()), 1.0);
        if (dis(gen) <= acceptance_probability) {
            currentSimplex = nextSimplex;
            neighbors = nextNeighbors;
        }

    }

    // Print the new simplex
    // cout << "{ ";
    // for (int v : currentSimplex) cout << v << " ";
    // cout << "}\n";
    return currentSimplex;
}

void approximateSFD(vector<vector<int>>& simplices, int samples) {
    int steps = 20; // Convert string to int
    vector<int> sfd;
    sfd.resize(19);

    for (int i= 0; i < samples; i++) {
        set<int> simplex = randomWalk(simplices, steps);
        sfd[findSimpletIndex(hashSimplex(simplex))]++;
    }

    // Print SFD
    cout << "{ ";
    for (int i= 1; i <= 18; i++) cout << static_cast<double>(sfd[i])/static_cast<double>(samples) << " ";
    cout << "}\n";
}

int main(int argc, char* argv[]) {
  // Load args
  if (argc != 5) {
      cerr << "Usage: " << argv[0] << " <simplex size input> <simplex vertices input> <steps>\n";
      return 1;
  }

  string inputFile1 = argv[1];
  string inputFile2 = argv[2];
  int n = atoi(argv[3]);  // Convert string to int
  int samples = atoi(argv[4]); // Convert string to int

  // For debug / test:
  cout << "Input file 1: " << inputFile1 << endl;
  cout << "Input file 2: " << inputFile2 << endl;
  cout << "Samples: " << formatNumber(samples) << endl;
  cout << "N: " << formatNumber(n) << endl;


  // Load the Complex
  load_simplices(inputFile1, inputFile2);
  construct_all_neighbors();
  vector<int> connectedVertices = selectConnectedVertices(all_nei, n);
  // Filter simplices that contain only vertices from connectedVertices
  filterSimplices(all_simplices, connectedVertices);

  // Construct the Complex
  auto start_time = chrono::high_resolution_clock::now(); // ⏱️ Start timing
  construct_complex();
  auto end_time = chrono::high_resolution_clock::now(); // ⏱️ End timing
  auto duration_load = chrono::duration_cast<chrono::milliseconds>(end_time - start_time);

  // Complex Properties
  // start_time = chrono::high_resolution_clock::now(); // ⏱️ Start timing
  fastGraphProperties(nei);
  // end_time = chrono::high_resolution_clock::now(); // ⏱️ End timing
  // auto duration_properties = chrono::duration_cast<chrono::milliseconds>(end_time - start_time);

  // Random Walk
  start_time = chrono::high_resolution_clock::now(); // ⏱️ Start timing
  approximateSFD(simplices, samples);
  end_time = chrono::high_resolution_clock::now(); // ⏱️ End timing
  auto duration_randomwalk = chrono::duration_cast<chrono::milliseconds>(end_time - start_time);

  cout << "\n⚡ Execution times:\n";
  cout << " Construction: " << formatNumber(duration_load.count()) << " ms" << endl;
  // cout << "Complex Properties: " << formatNumber(duration_properties.count()) << " ms" << endl;
  cout << "Random Walk: " << formatNumber(duration_randomwalk.count()) << " ms" << endl;
  return 0;
}
