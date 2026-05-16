# Contributing to Supermarket Analytics

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing.

## 🤝 Ways to Contribute

### 1. Report Issues
Found a bug? Have a suggestion? [Open an issue](https://github.com/yourusername/supermarket-analytics/issues)

**Include:**
- Clear description of the problem
- Steps to reproduce (if applicable)
- Expected vs. actual behavior
- Python version and OS
- Relevant error messages or screenshots

### 2. Submit Code
Want to add a feature or fix a bug?

**Process:**
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Test thoroughly
5. Commit with clear messages: `git commit -m "Add: description of changes"`
6. Push to your branch: `git push origin feature/your-feature-name`
7. Open a Pull Request

### 3. Improve Documentation
- Fix typos or unclear sections
- Add examples
- Improve explanations
- Translate to other languages

### 4. Add Analysis Sections
Create new analytical approaches:
- Machine learning models
- Predictive analytics
- Advanced statistical methods
- Custom visualizations

---

## 📋 Pull Request Guidelines

### Before Submitting
- [ ] Code follows PEP 8 style guide
- [ ] Added/updated docstrings
- [ ] Tested with different datasets
- [ ] No breaking changes to existing functionality
- [ ] Committed with clear messages

### PR Description Include
- **What:** Summary of changes
- **Why:** Motivation and use cases
- **How:** Brief explanation of implementation
- **Testing:** How you tested it
- **Closes:** Links to related issues (e.g., "Closes #123")

### Example PR Template
```markdown
## What
Added machine learning classification for customer churn prediction

## Why
Enables proactive customer retention strategies by identifying at-risk customers

## How
- Trained Random Forest classifier on historical data
- Achieved 85% accuracy on test set
- Added visualization of feature importance

## Testing
- Tested on original dataset: ✅ Passed
- Tested on new sample data: ✅ Passed

## Closes
#42 - Add churn prediction analysis
```

---

## 💻 Development Setup

### 1. Fork & Clone
```bash
git clone https://github.com/YOUR-USERNAME/supermarket-analytics.git
cd supermarket-analytics
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Development Dependencies
```bash
pip install -r requirements.txt
pip install pytest black flake8  # For testing and linting
```

### 4. Create Feature Branch
```bash
git checkout -b feature/your-feature-name
```

---

## 🧪 Testing

### Run Tests
```bash
pytest tests/
```

### Manual Testing
```python
# Test your code in Jupyter
import pandas as pd
from your_new_module import your_function

# Test with sample data
df = pd.read_csv('data/SuperMarket_Analysis.csv')
result = your_function(df)
print(result)
```

### Code Quality
```bash
# Check style
flake8 scripts/

# Format code
black scripts/
```

---

## 📝 Coding Standards

### Style Guide
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use descriptive variable names
- Add comments for complex logic
- Keep functions focused and small

### Documentation
```python
def analyze_customer_churn(sales_df, threshold=0.2):
    """
    Identify at-risk customers using transaction recency.
    
    Parameters
    ----------
    sales_df : pd.DataFrame
        Sales data with columns: ['Date', 'CustomerID', 'Revenue']
    threshold : float, default=0.2
        Recency threshold (0.2 = 20% of max recency)
    
    Returns
    -------
    pd.DataFrame
        Customers with churn probability scores
    
    Examples
    --------
    >>> churn_df = analyze_customer_churn(sales)
    >>> print(churn_df.head())
    """
    # Implementation...
```

### Comments
```python
# Good: Explains why
if transaction_value > threshold:
    # Flag as outlier because it's 3x average (potential fraud)
    is_outlier = True

# Bad: States obvious
if transaction_value > threshold:
    # Check if above threshold
    is_outlier = True
```

---

## 🎯 Contribution Ideas

### Beginner-Friendly
- [ ] Add more example datasets
- [ ] Improve documentation
- [ ] Fix typos
- [ ] Add unit tests
- [ ] Create tutorials

### Intermediate
- [ ] Add new visualization types
- [ ] Create interactive Jupyter widgets
- [ ] Add data validation
- [ ] Optimize performance
- [ ] Add logging

### Advanced
- [ ] Machine learning models
- [ ] Real-time streaming analysis
- [ ] REST API implementation
- [ ] Docker containerization
- [ ] Dashboard (Streamlit/Plotly)

---

## 📦 Project Structure

```
supermarket-analytics/
├── scripts/
│   ├── supermarket_advanced_analysis.py
│   ├── supermarket_visualizations.py
│   └── supermarket_implementation_guide.py
├── tests/
│   ├── test_analysis.py
│   └── test_visualizations.py
├── notebooks/
│   ├── analysis.ipynb
│   └── implementation_guide.ipynb
├── data/
│   └── SuperMarket_Analysis.csv
└── docs/
```

---

## 🔄 Commit Message Standards

### Format
```
[Type]: Short description

Optional longer description explaining why and how.

Closes #issue-number
```

### Types
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `test:` Tests
- `refactor:` Code restructuring
- `perf:` Performance improvement

### Examples
```bash
git commit -m "feat: Add customer churn prediction model"
git commit -m "fix: Correct date parsing error in analysis"
git commit -m "docs: Update README with new features"
git commit -m "test: Add unit tests for RFM calculation"
```

---

## 🚀 Release Process

1. Update version in `setup.py`
2. Update `CHANGELOG.md`
3. Create annotated tag: `git tag -a v1.0.0 -m "Version 1.0.0"`
4. Push tag: `git push origin v1.0.0`
5. GitHub Actions auto-publishes to PyPI

---

## 📞 Questions?

- 💬 Start a [Discussion](https://github.com/yourusername/supermarket-analytics/discussions)
- 📧 Email: your.email@example.com
- 📖 Check [README.md](README.md) and docs/

---

## ✅ Contributor Checklist

Before submitting your contribution:

- [ ] Code follows project style guide
- [ ] Documentation is updated
- [ ] Tests pass locally
- [ ] No unrelated changes included
- [ ] Commit messages are clear
- [ ] PR description explains changes
- [ ] You've read this guide

---

## 🎉 Thank You!

Your contributions help make this project better for everyone. We appreciate your time and effort!

---

**Last Updated:** 2024
