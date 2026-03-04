from fastapi import APIRouter, Depends, HTTPException
from .. import schemas, dependencies, models
import requests

router = APIRouter(
    prefix="/text-correction",
    tags=["text-correction"]
)

@router.post("/", response_model=schemas.TextCorrectionResponse)
async def correct_text(
    request: schemas.TextCorrectionRequest,
    current_user: models.User = Depends(dependencies.get_current_user)
):
    """
    Correct grammar and spelling using LanguageTool API (free, no API key needed)
    """
    try:
        # Use the free LanguageTool API
        api_url = "https://api.languagetool.org/v2/check"
        
        # Prepare the request
        data = {
            'text': request.text,
            'language': 'en-US'
        }
        
        # Make the request to LanguageTool
        response = requests.post(api_url, data=data, timeout=30)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail=f"LanguageTool API error: {response.text}"
            )
        
        result = response.json()
        
        # Apply corrections to the text
        corrected_text = request.text
        matches = result.get('matches', [])
        
        # Sort matches by offset in reverse order to apply corrections from end to start
        # This prevents offset shifts when making replacements
        matches_sorted = sorted(matches, key=lambda x: x['offset'], reverse=True)
        
        for match in matches_sorted:
            if match.get('replacements'):
                # Get the first suggested replacement
                replacement = match['replacements'][0]['value']
                offset = match['offset']
                length = match['length']
                
                # Replace the error with the correction
                corrected_text = (
                    corrected_text[:offset] + 
                    replacement + 
                    corrected_text[offset + length:]
                )
        
        return schemas.TextCorrectionResponse(
            original_text=request.text,
            corrected_text=corrected_text
        )
        
    except requests.exceptions.Timeout:
        raise HTTPException(
            status_code=504,
            detail="Grammar check service timed out. Please try again."
        )
    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error connecting to grammar check service: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing text correction: {str(e)}"
        )
