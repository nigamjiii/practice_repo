#include <bits/stdc++.h>
using namespace std;

// Macros for common operations
#define fastio() ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)
#define ll long long
#define ull unsigned long long
#define pb push_back
#define all(v) (v).begin(), (v).end()
#define sz(x) ((int)(x).size())
#define f first
#define s second
#define pii pair<int, int>
#define pll pair<ll, ll>
#define vi vector<int>
#define vl vector<ll>
#define vvi vector<vector<int>>
#define vvl vector<vector<ll>>
#define mii map<int, int>
#define mll map<ll, ll>

// Constants
const int MOD = 1e9 + 7;
const ll INF = 1e18;
const double EPS = 1e-9;

// Utility functions
template<typename T> void print_vec(const vector<T>& v) {
    for (auto& x : v) cout << x << " ";
    cout << "\n";
}

template<typename T1, typename T2> void print_map(const map<T1, T2>& m) {
    for (auto& p : m) cout << p.first << ": " << p.second << "\n";
}

// Power function with modular arithmetic
ll mod_pow(ll base, ll exp, ll mod = MOD) {
    ll res = 1;
    while (exp) {
        if (exp % 2) res = (res * base) % mod;
        base = (base * base) % mod;
        exp /= 2;
    }
    return res;
}

// GCD and LCM
ll gcd(ll a, ll b) { return b == 0 ? a : gcd(b, a % b); }
ll lcm(ll a, ll b) { return (a / gcd(a, b)) * b; }

// Main solve function
void solve() {
    // Write your solution here
}

// Main function
int main() {
    fastio();

    int t = 1;  // Change this to `cin >> t;` if there are multiple test cases
    while (t--) {
        solve();
    }
    return 0;
}
